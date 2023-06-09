#!/bin/bash
#cluster check
clustername=
[ "`pwd | grep '/home/users/dsw/'`" ] && clustername=ccfep
[ "`pwd | grep '/home/20/kazuma/'`" ] && clustername=qcl

#set variables
export RefDir=~kazuma/clones
export geomroot=~kazuma/clones/geom2
export orcaroot=~kazuma/clones/orcapack
export dir=.
tmps=(pf_benzalkane2 pyfile_general cbi)
for tmp in ${tmps[@]}; do
    geomdirs="${geomdirs[@]} ${geomroot}/${tmp}"
done
export geomdirs
. ${orcaroot}/func_Oclone.sh
. ~/clones/com/com_func.sh 
usecore=16
omp=1
nchain=1
is_chain=n
scf_niter=125

cp ${RefDir}/qsub.sh $dir
chmod +x $dir/qsub.sh
while read -a line; do
    [ -z ${line} ] && continue
    [ ${line:0:1} != '@' ] && continue
    #[ "`echo ${line[@]} | grep '!!'`" ] && continue
    [ ${line:0:2} = '@@' ] && {
        [ "`echo $opt | grep 'usecore='`" ] && usecore=${opt:8}
        [ "`echo $opt | grep 'omp='`" ] && omp=${opt:4}
        continue
    }
    line[0]=${line[0]:1}
    names=
    echo '$OCinp chechking --------------------'
    . ${orcaroot}/OReadInp.sh ${line[@]} # OReadInp
    
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'"
        exit 1
    }
    echo $names
    echo '$input modification --------------------'
    for name in $names; do
        charge=0
        mult=1
        keyword=
        #echo $name
        splited_name=(${name//_/ })
        MolName=${splited_name[0]}
        #for tmp in ${geomdirs}; do
        #    [ -e "${tmp}/${MolName}.py" ] && tmpdir=${tmp}
        #done
        #cp ${orcaroot}/orcabase.inp $dir/$name.inp
        #echo $MolName
        func_xyz2orca $name $MolName # xyz to inp
        #sed -i -e "s/chk=/chk=$name.chk/g" $dir/$name.gjf
        sed -i -e "s/_aug_np/$usecore/g" $dir/$name.inp
        . ${orcaroot}/modinp.sh
        #sed -i -e 's/ jobtype//g' $dir/$name.gjf 
        if [ ${is_chain} = y ]; then
            :
        else
            if [ $clustername = qcl ]; then
                cp ${orcaroot}/orcash.sh $dir/$name.sh
                sed -i -e "s/JOBNAME=.*/JOBNAME=${name}/g" $dir/${name}.sh
            elif [ $clustername = ccfep ]; then
                cp ${orcaroot}/orcash.sh $dir/$name.sh
                sed -i -e "s/JOBNAME=.*/JOBNAME=${name}/g" $dir/${name}.sh
            fi
        fi
    done # end of one file edit
    
    if [ ${is_chain} = y ] ; then
        cp ${orcaroot}/orcash_chain.sh $dir/Chain${nchain}.sh
        [ ${names:0:1} =  ] && names=${names# }
        sed -i -e "s/JOBNAMES=/JOBNAMES=${names}/g" $dir/Chain${nchain}.sh
        sed -i -e "s/filelist=(/filelist=(Chain${nchain} /g" $dir/qsub.sh
        sed -i -e "s/usecore=.*/usecore=${usecore}/g" $dir/qsub.sh
        sed -i -e "s/omp=.*/omp=${omp}/g" $dir/qsub.sh
        nchain=`expr $nchain + 1`
        is_chain=n
    else
        if [ $clustername = qcl ]; then
            sed -i -e "s/filelist=(/filelist=(${names} /g" $dir/qsub.sh
            sed -i -e "s/usecore=.*/usecore=${usecore}/g" $dir/qsub.sh
            sed -i -e "s/omp=.*/omp=${omp}/g" $dir/qsub.sh
        elif [ $clustername = ccfep ]; then
            
        fi
    fi
done < $orcaroot/OCinp # end of all line loop
