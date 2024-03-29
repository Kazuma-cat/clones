#!/bin/bash
# inner functions
infuncs_calc_detHn(){
    moltype=$1
    Cn=$2
    detCn=0
    case $moltype in
        polyene)
            detHn=`expr $Cn + 2` ;;
        benz-polyene)
            detHn=`expr $Cn + 2` ;;
        benz-alkane)
            detHn=`expr $Cn \* 2 + 2` ;;
    esac
    echo $detHn
}
infuncs_molNmod_CnHn(){
    MolName=$1
    moltype=$2
    tmps=(${MolName//_/ })
    Cmin=${tmps[1]:-0}
    Cmax=${tmps[2]:-300}
    echo "Cmin, Cmax = ${Cmin}, ${Cmax}" > ~/trash/Oclone.tr
    for tmp in ${geomdirs}; do
        filenames=(${filenames[@]} `ls ${tmp}/benz-c*.xyz`) 
    done
    names=()
    for filename in ${filenames[@]}; do
        filename=`basename ${filename}`
        Cn=`echo $filename | grep -o 'c[0-9]\+'`
        Hn=`echo $filename | grep -o 'h[0-9]\+'`
        Cn=${Cn:1}
        Hn=${Hn:1}
        detHn=`infuncs_calc_detHn $moltype $Cn`
        [ ${Hn} -eq ${detHn} ] && [ ${Cn} -ge ${Cmin} ] && [ ${Cn} -le ${Cmax} ] && {
            names="${names[@]} ${filename%.xyz}"
        }
    done
    echo $names
    echo $names >> ~/trash/Oclone.tr
}

# external functions
funcs_molNmod(){
    # 'names' is output variable
    MolName=$1
    moltype=(${MolName//_/ })
    moltype=${moltype[0]}
    case $moltype in
        polyene)
            names=`infuncs_molNmod_CnHn $MolName $moltype`;;
        benz-polyene)
            names=`infuncs_molNmod_CnHn $MolName $moltype`;;
        benzalk)
            names=`infuncs_molNmod_CnHn $MolName $moltype`;;
        *)
            names=$MolName
            names="$MolName"
            tmp=${MolName//'-'/'/'}
            xyzpath=$geomroot/$tmp.xyz
            [ -f $xyzpath ] || ls $xyzpath
    esac
    echo $names
}
func_xyz2orca(){
    name=$1
    MolName=$2
    geompath=`geomdet $MolName`
    #if [ `echo $MolName | grep cbi-` ]; then
    #    MolName=${MolName#'cbi-'}
    #    #name=${name#'cbi-'}
    #    tmpdir=${geomroot}/cbi
    #elif [ `echo $MolName | grep cbl-` ]; then
    #    MolName=${MolName#'cbl-'}
    #    #name=${name#'cbl-'}
    #    tmpdir=${geomroot}/cbl
    #else
    #    for tmp in ${geomdirs}; do
    #        [ -e "${tmp}/${MolName}.xyz" ] && tmpdir=${tmp}
    #    done
    #fi
    cp ${orcaroot}/orcabase.inp $dir/$name.inp
    geom=
    Nline=1
    while read -a line || [ -n $line ]; do
        [ -z ${line} ] && break
        [ $Nline -eq 2 ] && { echo ${line[@]};Nline=`expr $Nline + 1`;continue; }
        [ ${#line[@]} != 4 ] && { Nline=`expr $Nline + 1`;continue;}
        line=${line//}
        geom="${geom}${line[@]}\n"
        Nline=`expr $Nline + 1`
    done < $geompath #${tmpdir}/${MolName}.xyz
    sed -i -e "s/geom/$geom/g" $dir/$name.inp
}

