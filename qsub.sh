#!/bin/bash
qn > qn.tmp
usecore=max
omp=2
fillnode=n
n_node=1
option=${1:-default}
skip_nodes=
case $option in
    default)
        ini_node=k00
        end_node=k19 ;;
    a)
        ini_node=h01
        end_node=k28 ;;
    i)
        ini_node=i00
        end_node=i03 ;;
    ni)
        ini_node=h01
        end_node=k28
        skip_nodes="i00 i01 i02 i03"
        ;;
    *)
        echo "Error: undefined option '$option'"
        exit 1
esac
count=0
onskip=1
nodes=()
ncpus=()
while read -a qns; do
    [ $count -eq 0 ] && {
        count=`expr "$count" + 1`
        continue;
    }
    # determine the beggining point
    [ $onskip -eq 1 ] && {
        if [ ${qns[0]} = ${ini_node} ]; then
            onskip=0
        else
            continue
        fi
    }
    # determine the end point
    [ $onskip = 0 ] && {
        [ ${qns[0]} = ${end_node} ] && {
            onskip=1
        }
    }
    # skip node
    [ ${qns[0]} = k02 ] && continue
    [ ${qns[0]} = h04 ] && continue
    [ ${qns[0]} = h06 ] && continue
    [ "`echo ${skip_nodes} | grep ${qns[0]}`" ] && continue
    # get free nodes
    [ ${qns[1]} = free ] && {
        # avoid nodes which have some jobs
        [ ${#qns[@]} -eq 7 ] && {
            threshcore=$usecore
            if [ $fillnode = y ] && [ -$usecore != -max ]; then
                # get free node to fill its CPU
                while [ $threshcore -le `expr ${qns[3]} - 2` ]; do threshcore=`expr "$threshcore" + "$usecore"`; nodes=(${nodes[@]} ${qns[0]}); done
            else
                # get free node a time for each node
                nodes=(${nodes[@]} ${qns[0]})
                ncpus=(${ncpus[@]} ${qns[3]})
            fi
        }
    }
done < qn.tmp
echo "free nodes = ${nodes[@]}"
rm qn.tmp
count=0
filelist=()
qsublog=
recname=`realpath $0`
recname=${recname//.sh/.log}
#date > qsublog
date | tee -a ~/record/qsublog.rec $recname
pwd | tee -a ~/record/qsublog.rec $recname
# submit jops to each free node
[ ${#filelist[@]} -gt ${#nodes[@]} ] && { echo 'free nodes are too little compared with inputs'; exit 1; }
for file in ${filelist[@]}; do
    i_node=1
    while [ ${i_node} -le ${n_node} ]; do
        node=${nodes[$count]}
        [ -z $node ] && {
            echo 'free nodes are too little compared with inputs'
            exit 1
        }
        ncore=default
        if [ x$usecore = xmax ]; then
            ncore=${ncpus[$count]}
        else
            ncore=$usecore
        fi
        usenode="${node}:ppn=${ncore}"
        if [ ${i_node} -eq 1 ]; then
            nodeoption="nodes=${usenode}"
        elif [ ${i_node} -ge 2 ]; then
            nodeoption="${nodeoption}+${usenode}"
        else
            echo 'Error: inappropriate i_node value'
        fi
        i_node=`expr ${i_node} + 1`
        let ++count
    done
    #{
    #    echo "${nodeoption}"
    #    echo "${file}.sh"
    #} | tee -a qsublog ~/record/qsublog.rec $recname
    echo "qsub -l ${nodeoption} -v OMP=$omp $file.sh" | tee -a ~/record/qsublog.rec $recname
    #qsub -l nodes=${node}:ppn=${usecore} $file.sh
    qsub -l "${nodeoption}" -v OMP=$omp $file.sh | tee -a ~/record/qsublog.rec $recname
    echo '' | tee -a qsublog ~/record/qsublog.rec $recname
done
