#!/bin/bash
# check whether molecule original python script in clone directory
count=0
opt_method="PMPAO FBPAO newPAO oldPAO Ref RIMP2 NEVPT2 PNO-NEVPT2 calctest casscf b3lyp"
opt_moread="moreadonly moread-sto3g moread-sto3g-lowspin moread-b3lyp-lowspin moread-b3lyp-sto3g-def2svp-lowspin moread2-b3lyp-sto3g-def2svp-lowspin moread-reorder-b3lyp-sto3g-def2svp-lowspin moread-def2svp moread-def2svp-reorder moread2-def2svp-reorder moread-loc-def2svp moread2-loc-def2svp moread-def2tzvp moread-locDV-cbl moread-cas-cbl-sto3g-def2svp-PNOCAS moread-casscf moread2-cbl-mycas2 moread2-cbl-mycasloc1 moread-testcas moread-MScas-cbls-sto6g-tzvpp moread-MScas2-cbls-sto6g-tzvpp maxloop0 moread-MScas3-cbls-svp-tzvpp moread-sto6g moread-sto6g-svp moread-sto6g-tzvpp moread-casscf-sto6g-svp moread-casscf-sto6g-tzvpp"
opt_other="orzgit2 orzmod chain distribute nolct MS5orz noGA3 CMO locCA locDV locnC DOIFabs"
#defined_opts="newPAO oldPAO Ref RIMP2 NEVPT2 PNO-NEVPT2 calctest casscf moreadonly moread-sto3g moread-sto3g-lowspin moread-b3lyp-lowspin moread-b3lyp-sto3g-def2svp-lowspin moread2-b3lyp-sto3g-def2svp-lowspin moread-reorder-b3lyp-sto3g-def2svp-lowspin moread-def2svp moread-def2svp-reorder moread2-def2svp-reorder moread-loc-def2svp moread2-loc-def2svp moread-def2tzvp moread-locDV-cbl moread-cas-cbl-sto3g-def2svp-PNOCAS moread-casscf moread2-cbl-mycas2 moread2-cbl-mycasloc1 moread-testcas maxloop0 chain distribute nolct MS5orz noGA3 CMO locCA locDV locnC b3lyp "
defined_opts="${opt_method} ${opt_moread} ${opt_other}"
detect_opt=n
for opt in $@; do
    # check whether molecule original python script in clone directory
    [ "$count" -eq 0 ] && {
        MolName="$opt"
        if [ ${MolName:0:7} = 'polyene' ]; then
            IFSBACK=$IFS
            IFS=_
            tmps=(${MolName})
            IFS=$IFSBACK
            Cmin=${tmps[1]:-0}
            Cmax=${tmps[2]:-300}
            for tmp in ${pydirs[@]}; do
                filenames=(${filenames[@]} `ls ${tmp}/c*.py`)
            done
            #filenames=(`ls ${PyDir1}c*.py` `ls ${PyDir2}c*.py`)
            names=
            for filename in ${filenames[@]}; do
                filename=`basename ${filename}`
                Cn=`echo $filename | grep -o 'c[0-9]\+'`
                Hn=`echo $filename | grep -o 'h[0-9]\+'`
                Cn=${Cn:1}
                Hn=${Hn:1}
                HnM2=`expr ${Hn} - 2`
                [ ${Cn} -eq ${HnM2} ] && [ ${Cn} -ge ${Cmin} ] && [ ${Cn} -le ${Cmax} ] && {
                    names="${names[@]} ${filename%.py}"
                    #echo ${names[@]}
                }
                
            done
        elif [ ${MolName:0:12} = 'benz-polyene' ]; then
            IFSBACK=$IFS
            IFS=_
            tmps=(${MolName})
            IFS=$IFSBACK
            Cmin=${tmps[1]:-0}
            Cmax=${tmps[2]:-300}
            filenames=(`ls ${PyDir1}benz-c*.py` `ls ${PyDir2}benz-c*.py`)
            names=
            for filename in ${filenames[@]}; do
                filename=`basename ${filename}`
                Cn=`echo $filename | grep -o 'c[0-9]\+'`
                Hn=`echo $filename | grep -o 'h[0-9]\+'`
                Cn=${Cn:1}
                Hn=${Hn:1}
                HnM2=`expr ${Hn} - 2`
                [ ${Cn} -eq ${HnM2} ] && [ ${Cn} -ge ${Cmin} ] && [ ${Cn} -le ${Cmax} ] && {
                    names="${names[@]} ${filename%.py}"
                    #echo ${names[@]}
                }
                
            done
        elif [ ${MolName:0:11} = 'benz-alkane' ]; then
            IFSBACK=$IFS
            IFS=_
            tmps=(${MolName})
            IFS=$IFSBACK
            Cmin=${tmps[1]:-0}
            Cmax=${tmps[2]:-300}
            for tmp in ${pydirs}; do
                filenames=(${filenames[@]} `ls ${tmp}/benz-c*.py`)
            done
            names=
            for filename in ${filenames[@]}; do
                filename=`basename ${filename}`
                Cn=`echo $filename | grep -o 'c[0-9]\+'`
                Hn=`echo $filename | grep -o 'h[0-9]\+'`
                Cn=${Cn:1}
                Hn=${Hn:1}
                Cn2P2=`expr ${Cn} \* 2 + 2`
                [ ${Hn} -eq ${Cn2P2} ] && [ ${Cn} -ge ${Cmin} ] && [ ${Cn} -le ${Cmax} ] && {
                    names="${names[@]} ${filename%.py}"
                }
                
            done
         else
            names="$MolName"
            tmpchk=n
            for tmp in ${pydirs}; do
                [ -e "${tmp}/${MolName}.py" ] && tmpchk=y
            done
            [ $tmpchk = n ] && { echo "Name Error: ${MolName}.py could not be found."; exit 1; }
        fi
        
        count=`expr "$count" + 1`
        continue;
    } # molname loop end
    detect_opt=n
    for defined_opt in ${defined_opts}; do
        [ $opt = chain ] && [ $is_fullpack = y ] && { detect_opt=y; break; }
        [ $opt = $defined_opt ] && {
            tmps="${names}"
            names=
            for tmp in "${tmps[@]}"; do
                tmp2=${tmp}_${defined_opt}
                names="${names[@]} $tmp2"
            done
            detect_opt=y
        }
    done
    [ $detect_opt = y ] && continue
    [ "`echo $opt | grep 'ImplTypePM'`" ] && {
        case $opt in
            ImplTypePM)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_incore
                    tmp2=${tmp}_MS
                    names="${names[@]} $tmp1 $tmp2"
                done ;;
            ImplTypePM=incore)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_incore
                    names="${names} ${tmp1}"
                done ;;
            ImplTypePM=MS)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_MS
                    names="${names[@]} $tmp1"
                done ;;
        esac
    }
    [ "`echo $opt | grep 'OnTheFly'`" ] && {
        case $opt in
            OnTheFly)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_NotOn
                    tmp2=${tmp}_On
                    names="${names[@]} $tmp1 $tmp2"
                done ;;
            OnTheFly=On)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_On
                    names="${names[@]} $tmp2"
                done ;;
            OnTheFly=Not)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_NotOn
                    names="${names[@]} $tmp2"
                done ;;
        esac
    }
    [ "`echo $opt | grep 'ChargeType'`" ] && {
        case $opt in
            ChargeType)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_Mull
                    tmp2=${tmp}_Low
                    names="${names[@]} $tmp1 $tmp2"
                done ;;
            ChargeType=Mull)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_Mull
                    names="${names[@]} $tmp2"
                done ;;
            ChargeType=Low)
                tmps="${names[@]}"
                names=
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_Low
                    names="${names[@]} $tmp2"
                done ;;
        esac
    }
    [ "`echo $opt | grep 'LocMet'`" ] && {
        tmpLoc=${opt:7}
        IFSBACK=$IFS
        IFS=,
        tmpsLoc=(${tmpLoc})
        IFS=$IFSBACK
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpLoc in ${tmpsLoc[@]}; do
                tmp1=${tmp}_${tmpLoc}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'Tl'`" ] && {
        tmpl=${opt:3}
        IFSBACK=$IFS
        IFS=,
        tmpsl=(${tmpl})
        IFS=$IFSBACK
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpl in ${tmpsl[@]}; do
                tmp1=${tmp}_Tl${tmpl}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'Tj'`" ] && {
        tmpj=${opt:3}
        IFSBACK=$IFS
        IFS=,
        tmpsj=(${tmpj})
        IFS=$IFSBACK
        tmps="${names[@]}"
        names=()
        for tmp in "${tmps[@]}"; do
            for tmpj in ${tmpsj[@]}; do
                tmp1=${tmp}_Tj${tmpj}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'Tr'`" ] && {
        tmpr=${opt:3}
        IFSBACK=$IFS
        IFS=,
        tmpsr=(${tmpr})
        IFS=$IFSBACK
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_Tr${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'TCutPNOrho0'`" ] && {
        tmpr=${opt:12}
        IFSBACK=$IFS
        IFS=,
        tmpsr=(${tmpr})
        IFS=$IFSBACK
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_TCutPNOrho0${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'TCutPairs'`" ] && {
        tmpr=${opt:10}
        IFSBACK=$IFS
        IFS=,
        tmpsr=(${tmpr})
        IFS=$IFSBACK
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_TCutPairs${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'TCutPre'`" ] && {
        tmpr=${opt:8}
        IFSBACK=$IFS
        IFS=,
        tmpsr=(${tmpr})
        IFS=$IFSBACK
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_TCutPre${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'PMMaxIt='`" ] && {
        tmpr=${opt:8}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_PMMaxIt${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'PMStep='`" ] && {
        tmpr=${opt:7}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_PMStep${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'PMAB='`" ] && {
        tmpr=${opt:5}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_PMAB${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'PMang='`" ] && {
        tmpr=${opt:6}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_PMang${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'PMtrunc='`" ] && {
        tmpr=${opt:8}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_PMtrunc${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'lvlshift='`" ] && {
        tmpr=${opt:9}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_lvlshift${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'ipeashift='`" ] && {
        tmpr=${opt:10}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_ipeashift${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ "`echo $opt | grep 'lctmaxiter='`" ] && {
        tmpr=${opt:11}
        tmpsr=(${tmpr//','/ })
        tmps="${names[@]}"
        names=()
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_lctmaxiter${tmpr}
                names="${names[@]} $tmp1"
            done
        done
    }
    [ $opt = newPMtramix ] && {
        tmps="${names[@]}"
        names=
        angthresh="1e-4 1e-5 1e-6 1e-7"
        truncthresh="1e-1 1e-2 1e-3 1e-4"
        for tmp in "${tmps[@]}"; do
            for ang in ${angthresh}; do
                for trunc in ${truncthresh}; do
                    tmp1=${tmp}_PMtrunc${trunc}_PMang${ang}
                    names="${names[@]} $tmp1"
                done
            done
        done
    }
    
    #Form name of molecule basis
    [ "`echo $opt | grep 'Mbasis='`" ] && {
        tmps="${names[@]}"
        names=
        for tmp in "${tmps[@]}"; do
            tmp1=${tmp}_${opt}
            names="${names[@]} $tmp1"
        done
    }
    [ "`echo $opt | grep 'charge='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    [ "`echo $opt | grep 'mult='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    [ "`echo $opt | grep 'act='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    [ "`echo $opt | grep 'roots='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    [ "`echo $opt | grep 'StackSize='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    [ "`echo $opt | grep 'DOIPower='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    [ "`echo $opt | grep 'maxloop'`" ] && {
        tmps=(${names[@]})
        names=()
        for tmp in "${tmps[@]}"; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    count=`expr "$count" + 1`
done
echo ${names[@]}
