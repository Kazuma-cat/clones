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
. ${orcaroot}/func_Mclone.sh
# predefining argument  -----------------
usecore=16
omp=1
nchain=1
is_chain=n
#cp ${RefDir}qsub.sh $Dir
#chmod +x ${Dir}qsub.sh
# main process --------------------------
while read -a line; do
    [ -z ${line} ] && continue
    [ ${line[0:1]} != '@' ] continue
    [ ${line[0:2]} != '@@' ] && {
        for opt in ${line[@]}; do
            [ "`echo $opt | grep 'usecore='`" ] && usecore=${opt:8}
            [ "`echo $opt | grep 'omp='`" ] && omp=${opt:4}
            continue
        done
    }
    names=
    . ${molcroot}/MReadInp.sh ${line[@]} # OReadInp
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'"
        exit 1
    }
    for name in $names; do
        cp cp ${molcroot}/molcbase.input $dir/$name.input
        sed -i -e "s/TITLE=/TITLE=$name/g" $dir/$name.input;;
        sed -i -e "s/GROUP=/GROUP=nosym/g" $dir/$name.input;;
        name_spl_=(${name//_/ })
        molname=${name_spl_[0]}
        # fixed variable for case-----
        case_RASSCF="RASSCF(\d+,\d+)(\d+,\d+,\d+)(\d+,\d+,\d+)(\d+,\d+,\d+)"
        # ----------------------------
        for spl in ${splited_name[@]}; do
            case $spl in
                $molName)
                    geompaths=(`retgeompath $name $molname`)
                    cp ${geompaths[0]} $dir/$name.xyz
                    sed -i -e "s/COORD=/COORD=${geompaths[1]}/g" $dir/$name.input;;
                SVP)
                    sed -i -e "s/BASIS=/BASIS=SVP/g" $dir/$name.input;;
                TZVP)
                    sed -i -e "s/BASIS=/BASIS=TZVP/g" $dir/$name.input;;
                SCF)
                    sed -i -e "s/*tail/&SCF\n*tail/g" $dir/$name.input;;
                $case_RASSCF)
                    sed -i -e "s/*tail/&RASSCF\n*tail/g" $dir/$name.input
                    tmp=${spl//'('/ }
                    tmp=(${tmp//')'/ })
                    tmp1=(${tmp[1]//','/ });tmp3=(${tmp[3]//','/ });
                    charge=${tmp1[0]};mult=${tmp1[1]};
                    nactel=${tmp[2]}
                    ras1=${tmp3[0]};ras2=${tmp3[1]};ras3=${tmp3[2]};
                    ciroot=${tmp[4]}
                    norbs=(`readxyz $dir/$name.xyz`)
                    elclosed=$((${norbs[0]} + ${norbs[1]}))
                    tmp=`python -c print(($elclosed-$charge-${nactel[0]})/2)`
                    inactorb=`printf '%.0f\n' $closed`
                    sed -i -e "s/*tail/SPIN=$mult\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/NACTEL=$nactel\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/INACT=$inactorb\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/RAS1=$ras1\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/RAS2=$ras2\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/RAS3=$ras3\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/CIROOT=$ciroot\n*tail/g" $dir/$name.input
                    sed -i -e "s/*tail/LUMORB\n*tail/g" $dir/$name.input
                    ;;
                *)
                    ;;
            esac
            cp ${molcroot}/molcsh_fugu.sh $dir/$name.sh
        done # End spl
    done
done < $molcroot/MCinp
