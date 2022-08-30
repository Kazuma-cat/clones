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
        benz-alkane)
            names=`infuncs_molNmod_CnHn $MolName $moltype`;;
        *)
            names=$MolName
            tmpchk=n
            for tmp in ${geomdirs}; do
                [ -e "${tmp}/${MolName}.xyz" ] && tmpchk=y
            done
            [ $tmpchk = n ] && { echo "Name Error: ${MolName}.py could not be found."; exit 1; };;
    esac
    echo $names
}
func_xyz2gjf(){
    name=$1
    MolName=$2
    for tmp in ${geomdirs}; do
        [ -e "${tmp}/${MolName}.xyz" ] && tmpdir=${tmp}
    done
    cp ${gaussroot}/GaussBase.gjf $dir/$name.gjf
    geom=
    while read -a line || [ -n $line ]; do
        [ -z ${line} ] && break
        [ ${#line[@]} != 4 ] && { continue;}
        line=${line//}
        geom="${geom}${line[@]}\n"
    done < ${tmpdir}/${MolName}.xyz
    sed -i -e "s/geom/$geom/g" $dir/$name.gjf
}

