#!/bin/bash
# check whether molecule original python script in clone directory
count=0
for opt in $@; do
    # check whether molecule original python script in clone directory
    [ "$count" -eq 0 ] && {
        MolName="$opt";         
        names=($MolName)
        [ -e "${PyDir}${MolName}.py" ] || { echo "Name Error: ${MolName}.py could not be found."; exit 1; }
        count=`expr "$count" + 1`
        continue;
    }
    #Form name of ImplType
    [ "`echo $opt | grep 'ImplTypePM'`" ] && {
        case $opt in
            ImplTypePM)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_incore
                    tmp2=${tmp}_MS
                    names=("${names[@]}" $tmp1 $tmp2)
                done ;;
            ImplTypePM=incore)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_incore
                    names=("${names[@]}" $tmp1)
                done ;;
            ImplTypePM=MS)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_MS
                    names=("${names[@]}" $tmp1)
                done ;;
        esac
    }
    #Form name of isOnTheFly
    [ "`echo $opt | grep 'OnTheFly'`" ] && {
        case $opt in
            OnTheFly)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_NotOn
                    tmp2=${tmp}_On
                    names=("${names[@]}" $tmp1 $tmp2)
                done ;;
            OnTheFly=On)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_On
                    names=("${names[@]}" $tmp2)
                done ;;
            OnTheFly=Not)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_NotOn
                    names=("${names[@]}" $tmp2)
                done ;;
        esac
    }
    #Form name of ChargeType
    [ "`echo $opt | grep 'ChargeType'`" ] && {
        case $opt in
            ChargeType)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_Mull
                    tmp2=${tmp}_Low
                    names=("${names[@]}" $tmp1 $tmp2)
                done ;;
            ChargeType=Mull)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_Mull
                    names=("${names[@]}" $tmp2)
                done ;;
            ChargeType=Low)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_Low
                    names=("${names[@]}" $tmp2)
                done ;;
        esac
    }
    #Form name of LocMet
    [ "`echo $opt | grep 'LocMet'`" ] && {
        tmpLoc=${opt:7}
        IFSBACK=$IFS
        IFS=,
        tmpsLoc=(${tmpLoc})
        IFS=$IFSBACK
        tmps=(${names[@]})
        names=()
        for tmp in "${tmps[@]}"; do
            for tmpLoc in ${tmpsLoc[@]}; do
                tmp1=${tmp}_${tmpLoc}
                names=("${names[@]}" $tmp1)
                done
        done
    }
    #Form name of Thresh of jacobi
    [ "`echo $opt | grep 'Tj'`" ] && {
        tmpj=${opt:3}
        IFSBACK=$IFS
        IFS=,
        tmpsj=(${tmpj})
        IFS=$IFSBACK
        tmps=(${names[@]})
        names=()
        for tmp in "${tmps[@]}"; do
            for tmpj in ${tmpsj[@]}; do
                tmp1=${tmp}_Tj${tmpj}
                names=("${names[@]}" $tmp1)
                done
        done
    }
    #Form name of Thresh of NR macro iterarion
    [ "`echo $opt | grep 'Tl'`" ] && {
        tmpl=${opt:3}
        IFSBACK=$IFS
        IFS=,
        tmpsl=(${tmpl})
        IFS=$IFSBACK
        tmps=(${names[@]})
        names=()
        for tmp in "${tmps[@]}"; do
            for tmpl in ${tmpsl[@]}; do
                tmp1=${tmp}_Tl${tmpl}
                names=("${names[@]}" $tmp1)
            done
        done
    }
    #Form name of Thresh of davidson iteration
    [ "`echo $opt | grep 'Tr'`" ] && {
        tmpr=${opt:3}
        IFSBACK=$IFS
        IFS=,
        tmpsr=(${tmpr})
        IFS=$IFSBACK
        tmps=(${names[@]})
        names=()
        for tmp in "${tmps[@]}"; do
            for tmpr in ${tmpsr[@]}; do
                tmp1=${tmp}_Tr${tmpr}
                names=("${names[@]}" $tmp1)
            done
        done
    }
    #Form name of molecule basis
    [ "`echo $opt | grep 'Mbasis'`" ] && {
        case $opt in
            Mbasis=def2-SVP)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp1=${tmp}_def2svp
                    names=("${names[@]}" $tmp1)
                done ;;
            Nbasis=def2-TZVPP)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_def2tzvpp
                    names=("${names[@]}" $tmp2)
                done ;;
            Mbasis=cc-pvdz)
                tmps=(${names[@]})
                names=()
                for tmp in "${tmps[@]}"; do
                    tmp2=${tmp}_ccpvdz
                    names=("${names[@]}" $tmp2)
                done ;;
        esac
    }
    #Form name of moread
    [ "`echo $opt | grep 'moread'`" ] && {
        [ -e "${chkxDir}${MolName}.chkx" ] || { echo "Error: ${MolName}.chkx could not be found."; exit 1; }
        tmps=(${names[@]})
        names=()
        for tmp in "${tmps[@]}"; do
            tmp2=${tmp}_moread
            names=("${names[@]}" $tmp2)
        done
    }
    #Form name of maxloop0
    [ "`echo $opt | grep 'maxloop0'`" ] && {
        tmps=(${names[@]})
        names=()
        for tmp in "${tmps[@]}"; do
            tmp2=${tmp}_maxloop0
            names=("${names[@]}" $tmp2)
        done
    }
    count=`expr "$count" + 1`
done
echo ${names[@]}
