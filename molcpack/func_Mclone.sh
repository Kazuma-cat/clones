#!/bin/bash
export orcaroot=~kazuma/clones/orcapack
. ${orcaroot}/func_Oclone.sh
readxyz(){
    filename=$1
    filebase=`basename $filename`
    geom=
    frozen=0
    closed=0
    casclosed=0
    occ=0
    act=0
    Nline=0
    while read -a line || [ -n $line ]; do
        #echo $line
        [ $Nline -eq 0 ] && { Nline=`expr $Nline + 1`;continue;}
        [ $Nline -eq 1 ] && { Nline=`expr $Nline + 1`;continue;}
        [ -z $line ] && break
        [ ${#line[@]} != 4 ] && { echo ${#line[@]};Nline=`expr $Nline + 1`;continue;}
        geom="${geom}\nqatom(atom.${line[0]}, [${line[1]}, ${line[2]}, ${line[3]}]),"
        case ${line[0]} in
            H)
                closed=$((closed + 1));;
            C)
                frozen=$((frozen + 2))
                closed=$((closed + 4));;
            N)
                frozen=$((frozen + 2))
                closed=$((closed + 5));;
            O)
                frozen=$((frozen + 2))
                closed=$((closed + 6));;
            P)
                frozen=$((frozen + 10))
                closed=$((closed + 5));;
            S)
                frozen=$((frozen + 10))
                closed=$((closed + 6));;
            Cl)
                frozen=$((frozen + 10))
                closed=$((closed + 7));;
            Co)
                frozen=$((frozen + 10))
                closed=$((closed + 17));;
            Ni)
                frozen=$((frozen + 10))
                closed=$((closed + 18));;
            *)
                echo "detect undefined atom"
        esac
        Nline=`expr $Nline + 1`
    done < $filename
    #frozen="`echo "scale=2; $frozen/2 " | bc`"
    #closed="`echo "scale=2; $closed/2 " | bc`"
    #[ ${frozen: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    #[ ${closed: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    #frozen=`printf '%.0f\n' $frozen`
    #closed=`printf '%.0f\n' $closed`
    echo "$frozen $closed"
}
retgeompath(){
    name=$1
    MolName=$2
    if [ `echo $MolName | grep cbi-` ]; then
        MolName=${MolName#'cbi-'}
        #name=${name#'cbi-'}
        tmpdir=${geomroot}/cbi
    elif [ `echo $MolName | grep cbl-` ]; then
        MolName=${MolName#'cbl-'}
        #name=${name#'cbl-'}
        tmpdir=${geomroot}/cbl
    else
        for tmp in ${geomdirs}; do
            [ -e "${tmp}/${MolName}.xyz" ] && tmpdir=${tmp}
        done
    fi
    echo ${tmpdir}/${MolName}.xyz $MolName
}
