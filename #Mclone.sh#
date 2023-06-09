#!/bin/bash
[ "`pwd | grep 'clones'`" ] && { echo 'Do not employ Mclone.sh at the "clones" directory';}
# general setting -------------------------------
export RefDir=~kazuma/clones
export geomroot=~kazuma/clones/geom
export molcroot=~kazuma/clones/molcpack
export dir=.
tmps=(pf_benzalkane2 pyfile_general cbi)
for tmp in ${tmps[@]}; do
    geomdirs="${geomdirs[@]} ${geomroot}/${tmp}"
done
export geomdirs
. ${molcroot}/func_Mclone.sh

# predefining argument  -----------------
usecore=16
omp=1
nchain=1
is_chain=n
re_RASSCF="RASSCF-[0-9]+,[0-9]+--[0-9]+,[0-9]+,[0-9]+--[0-9]+,[0-9]+,[0-9]+--[0-9]+,[0-9]+,[0-9]+"
case_RASSCF="RASSCF-[0-9]*,[0-9]*--[0-9]*,[0-9]*,[0-9]*--[0-9]*,[0-9]*,[0-9]*--[0-9]*,[0-9]*,[0-9]*"
tmp="RASSCF-0,1--10,0,0--0,10,0--6,6,1"
tmp2="2"

# main process --------------------------
cp ${RefDir}/sbatch.sh $dir
cp ${RefDir}/cporb.sh $dir
#chmod +x ${Dir}/cporb.sh
chmod +x $dir/sbatch.sh
while read -a setline; do
    #cat $molcroot/MCinp
    [ -z ${setline} ] && continue
    line="${setline[@]}"
    [ ${line:0:1} != '@' ] && continue
    [ ${line:0:2} = '@@' ] && {
        for opt in ${line[@]}; do
            [ "`echo $opt | grep 'usecore='`" ] && usecore=${opt:8}
        done
        continue
    }
    line=${line:1}
    names=
    . ${molcroot}/MReadInp.sh ${line[@]} # OReadInp
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'.(in ${BASH_SOURCE[0]})"
        exit 1
    }
    for name in $names; do
        cp ${molcroot}/molcbase.input $dir/$name.input
        sed -i -e "s/TITLE=/TITLE=$name/g" $dir/$name.input
        sed -i -e "s/GROUP=/GROUP=nosym/g" $dir/$name.input
        name_spl_=(${name//_/ })
        molname=${name_spl_[0]}
        # fixed variable for case-----
        #case_RASSCF="RASSCF(\d+,\d+)(\d+,\d+,\d+)(\d+,\d+,\d+)(\d+,\d+,\d+)"
        # ----------------------------
        for spl in ${name_spl_[@]}; do
            case $spl in
                $molname)
                    geompaths=(`retgeompath $name $molname`)
                    cp ${geompaths[0]} $dir/$name.xyz
                    sed -i -e "s/COORD=/COORD=${name}.xyz/g" $dir/$name.input;;
                SVP)
                    sed -i -e "s/BASIS=/BASIS=SVP/g" $dir/$name.input;;
                TZVP)
                    sed -i -e "s/BASIS=/BASIS=TZVP/g" $dir/$name.input;;
                SCF)
                    sed -i -e "s/*tail/\&SCF\n\n*tail/g" $dir/$name.input;;
                $case_RASSCF)
                    sed -i -e "s/*tail/\&RASSCF\n*tail/g" $dir/$name.input
                    tmp=(${spl//'-'/ })
                    tmp1=(${tmp[1]//','/ });tmp3=(${tmp[3]//','/ });
                    charge=${tmp1[0]};mult=${tmp1[1]};
                    nactel=${tmp[2]}
                    ras1=${tmp3[0]};ras2=${tmp3[1]};ras3=${tmp3[2]};
                    ciroot=${tmp[4]}
                    norbs=(`readxyz $dir/$name.xyz`)
                    closedel=$((${norbs[0]} + ${norbs[1]}))
                    nactel1=${nactel//,*/ }
                    #tmp=`python -c print($elclosed-$charge-${nactel[0]}/2)`
                    tmp=`expr $closedel - $charge - $nactel1`
                    closedorb=`awk "BEGIN { print $tmp/2 }"`
                    #closedorb="`echo "scale=2; $tmp/2 " | bc`"
                    inactorb=`printf '%.0f\n' $closedorb`
                    sed -i -e "s/*tail/SPIN=$mult\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/NACTEL=$nactel\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/INACT=$inactorb\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/RAS1=$ras1\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/RAS2=$ras2\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/RAS3=$ras3\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/CIROOT=$ciroot\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/LUMORB\n\n*tail/g" $dir/$name.input
                    ;;
                *)
                    ;;
            esac
            cp ${molcroot}/molcsh_fugu.sh $dir/$name.sh
            sed -i -e "s/JOBNAME=.*/JOBNAME=${name}/g" $dir/${name}.sh
        done # End spl
        sed -i -e "s/filelist=(/filelist=(${names} /g" $dir/sbatch.sh
        sed -i -e "s/filelist=(/filelist=(${names} /g" $dir/cporb.sh
    done # End name
done < $molcroot/MCinp
echo "--- END Mclone ---"
