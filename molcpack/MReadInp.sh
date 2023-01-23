#!/bin/bash
# check whether molecule original python script in clone directory
count=0
defined_words="TZVP SVP"
opts_num=""
for opt in ${line[@]}; do
    # check whether molecule original python script in clone directory
    [ "$count" -eq 0 ] && {
        MolName="$opt"
        echo $MolName
        names=`funcs_molNmod $MolName`
        echo $names
        count=`expr "$count" + 1`
        continue;
    }
    # normal option detector ---------------------------------
    detect_word=n
    for defined_word in ${defined_words}; do
        #[ $word = chain ] && [ $is_fullpack = y ] && { detect_word=y; break; }
        [ $word = $defined_word ] && {
            tmps=(${names[@]})
            names=()
            for tmp in "${tmps[@]}"; do
                tmp2=${tmp}_${defined_word}
                names="${names[@]} $tmp2"
            done
            detect_word=y
            echo ${names}
        }
    done
    [ $detect_word = y ] && continue
    # number's option detector -------------------------------
    detect_optnum=n
    for opt_num in ${opts_num}; do
        #[ $opt = chain ] && [ $is_fullpack = y ] && { detect_opt=y; break; }
        [ `echo $opt | grep "${opt_num}="` ] && {
            tmps=${names}
            names=
            tmpset=(${opt//'='/' '})
            optspr=${tmpset[0]}
            optnums=${tmpset[1]//','/' ' }
            for optnum in ${optnums}; do
                for tmp in ${tmps}; do
                    tmp2=${tmp}_${optspr}=${optnum}
                    names="${names} $tmp2"
                done
            done
            detect_optnum=y
        }
    done
    [ $detect_optnum = y ] && continue
    # other option detector ----------------------------------------------------------------------------------
    [ `echo $opt | grep "RASSCF(\d+,\d+)(\d+,\d+,\d+)(\d+,\d+,\d+)(\d+,\d+,\d+)"` ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${opt}
            names="$names $tmpname"
        done
    }
    count=`expr "$count" + 1`
done
