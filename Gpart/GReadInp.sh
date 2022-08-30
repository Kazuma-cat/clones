#!/bin/bash
# check whether molecule original python script in clone directory
count=0
for word in ${line[@]}; do
    # check whether molecule original python script in clone directory
    [ "$count" -eq 0 ] && {
        MolName="$word"
        names=`funcs_molNmod $MolName`
        count=`expr "$count" + 1`
        continue;
    }
    # "names" is output variable
    case $word in
        opt)
            tmps=$names
            names=
            for tmp in $tmps; do
                tmpname=${tmp}_opt
                names="$names $tmpname"
            done ;;
        GD3BJ)
            tmps=$names
            names=
            for tmp in $tmps; do
                tmpname=${tmp}_GD3BJ
                names="$names $tmpname"
            done ;;
        b3lyp)
            tmps=$names
            names=
            for tmp in $tmps; do
                tmpname=${tmp}_b3lyp
                names="$names $tmpname"
            done ;;
        def2svp)
            tmps=$names
            names=
            for tmp in $tmps; do
                tmpname=${tmp}_def2svp
                names="$names $tmpname"
            done ;;
        chain)
            tmps=$names
            names=
            for tmp in $tmps; do
                tmpname=${tmp}_chain
                names="$names $tmpname"
            done ;;
        *)
            [ "`echo $word | grep 'mem'`" ] && {
                tmps=$names
                names=()
                for tmp in $tmps; do
                    tmpname=${tmp}_${word}
                    names="$names $tmpname"
                done
            }
    esac
    count=`expr "$count" + 1`
done
