#!/bin/bash
# check whether molecule original python script in clone directory
count=0
def_method='b3lyp b2plyp m06 tpssh STEOM-DLPNO-CCSD'
def_basis='def2-svp def2-tzvp '
def_other='D3BJ D3zero opt freq chain tightscf'
def_set="std-def2svp std-def2tzvp std-def2tzvpp std-def2qzvp std-def2qzvpp std2-sto3g std2-def2tzvpp RIMP2-def2svp RIMP2-def2tzvp RIMP2-def2tzvpp  SOSCF-KDIIS def2svp-RIJ rijcosx def2-tzvp-rijcosx"

defined_words="$def_method $def_basis $def_other $def_set"
#echo $defined_words
for word in ${line[@]}; do
    # check whether molecule original python script in clone directory
    [ "$count" -eq 0 ] && {
        MolName="$word"
        names=`funcs_molNmod $MolName`
        count=`expr "$count" + 1`
        continue;
    }
    # "names" is output variable
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
        }
    done
    [ $detect_word = y ] && continue
    
    [ "`echo $word | grep 'mem'`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${word}
            names="$names $tmpname"
        done
    }
    [ "`echo $word | grep 'charge='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${word}
            names="$names $tmpname"
        done
    }
    [ "`echo $word | grep 'mult='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${word}
            names="$names $tmpname"
        done
    }
    [ "`echo $word | grep 'scf-niter='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${word}
            names="$names $tmpname"
        done
    }
    [ "`echo $word | grep 'td=[0-9]\+-[0-9]\+'`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${word}
            names="$names $tmpname"
        done
    }
    [ "`echo $word | grep 'mdci='`" ] && {
        tmps=$names
        names=()
        for tmp in $tmps; do
            tmpname=${tmp}_${word}
            names="$names $tmpname"
        done
    }
    
    count=`expr "$count" + 1`
done
