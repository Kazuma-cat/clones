#!/bin/bash

# define function
xyz2orz(){
    filename=$1
    newfname=$2
    filebase=`basename $filename`
    geom=
    frozen=0
    closed=0
    casclosed=0
    occ=0
    act=0
    cp ~/clones/pybase.py ${newfname}
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
    #frozen=`python -c "print($frozen/2)"`
    frozen="`echo "scale=2; $frozen/2 " | bc`"
    closed="`echo "scale=2; $closed/2 " | bc`"
    #[ ${frozen: -1} -ne 0 || ${closed: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    [ ${frozen: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    [ ${closed: -1} -ne 0 ] && exit "uncorrect electron number was detected"
    sed -i -e "s/# orb info bgn ------------/# orb info bgn ------------\n# orig frozen ... ${frozen}\n# orig closed ... ${closed}/g" ${newfname}
    
    frozen=`printf '%.0f\n' $frozen`
    closed=`printf '%.0f\n' $closed`
    #echo "geom=${geom}"
    # active modification
    tmp=(${filename//\// })
    dir=${tmp[-2]}
    case $dir in
        pf_benzalkane2)
            act=3;;
        pyfile_benzalkane)
            act=3;;
        pyfile_benzalkane3)
            act=3;;
        pyfile_general)
            act=0
    esac
    closed=$((closed - act))
    occ=$((act * 2))
    casclosed=$((frozen + closed))
    sed -i -e "s/geom = \[/geom = \[${geom}/g" ${newfname}
    sed -i -e "s/acene = .*\[/acene = \[${geom}/g" ${newfname}
    sed -i -e "s/casscf.closed = \[0\]/casscf.closed = \[$casclosed\]/g" ${newfname}
    sed -i -e "s/casscf.occ = \[0\]/casscf.occ = \[$occ\]/g" ${newfname}
    sed -i -e "s/icmr.frozen = \[0\]/icmr.frozen = \[$frozen\]/g" ${newfname}
    sed -i -e "s/icmr.closed = \[0\]/icmr.closed = \[$closed\]/g" ${newfname}
    sed -i -e "s/icmr.occ = \[0\]/icmr.occ = \[$occ\]/g" ${newfname}
    
    
}

# main section
geomdir=~/clones/geom
pyFRgeomdir=~/clones/pyFRgeom
# process argumrnt
dirlist=
if [ $# -eq 0 ]; then
    alldir="`ls $geomdir`"
    alldir=`echo ${alldir} | sed -e s/[\r\n]\+/''/g`
    echo "You must enter argument. ('a', ${alldir//' '/', '})"
    exit 1
elif [ $# -eq 1 ] && [ $1 = a ]; then
    dirlist=`ls $geomdir`
else
    for tmpdir in $@; do
        [ `ls $geomdir | grep ${tmpdir}` ] && dirlist="${dirlist}${tmpdir} "
    done
fi
echo $dirlist
#skipdir="Cbl  pf_benzalkane2  pyfile_benzalkane  pyfile_benzalkane3  pyfile_general  pyfile_polyene"
#skiplist='H2P.py NF86-Di.py NF86-Mo.py NF86-Tet.py NF86-Tri.py'
[ y = y ] && {
    for geomdir2 in ${dirlist}; do
        is_skip=n
        for tmp in ${skipdir}; do
            for tmpdir in ${geomdir2};do
                [ $tmp = $tmpdir ] && is_skip=y
            done
        done
        [ $is_skip = y ] && { echo "${geomdir2} directory is skipped"; continue;}
        [ `echo ${geomdir2} | grep .false` ] && continue
        [ -d "${pyFRgeomdir}/${geomdir2}" ] || mkdir ${pyFRgeomdir}/${geomdir2}
        for filebase in `ls ${geomdir}/${geomdir2}`; do
            [ ${filebase: -1} = '~' ] && continue
            ## skip -------
            #is_skip=n
            #for tmp in ${skiplist}; do
            #    [ tmp = $filebase ] && is_skip=y
            #done
            #[ $is_skip = y ] && { echo "${filebase} is skipped"; continue;}
            # main -------
            #filename="${pydir}/${pydir2}/${filename}"
            filename="${geomdir}/${geomdir2}/${filebase}"
            newfname="${pyFRgeomdir}/${geomdir2}/${filebase//.xyz/.py}"
            echo $filename
            xyz2orz $filename $newfname
        done
    done
}
