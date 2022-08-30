#!/bin/bash

# defining function
orz2xyz(){
    filename=$1
    newfname=$2
    in_geom=n
    geom=
    natom=0
    filebase=`basename $filename`
    echo "natom" > ${newfname}
    echo "${filebase}" >> ${newfname}
    echo "geom" >> ${newfname}
    cat ${newfname}
    while read -a line; do
        [ ${#line} != 0 ] && [ ${line:0:1} = ']' ] && { in_geom=n; continue;}
        [ ${in_geom} = y ] && {
            atom=${line%%,*}
            atom=${atom##*.}
            [ -z $atom ] || natom=`expr $natom + 1`
            xyz=${line[@]%\]*}
            xyz=${xyz#*\[}
            xyz=${xyz// /}
            xyz=(${xyz//,/ })
            [ ${xyz[0]} = 0 ] && xyz[0]=0.0
            [ ${xyz[1]} = 0 ] && xyz[1]=0.0
            [ ${xyz[2]} = 0 ] && xyz[2]=0.0
            xyzline="${atom} ${xyz[@]}"
            geom="$geom$xyzline\n"
        }
        [ ${#line} -ge 4 ] && [ ${line:0:4} = geom ] && in_geom=y
        [ ${#line} != 0 ] && [ ${line:0:1} = ']' ] && { in_geom=n; continue;}
    done < ${filename}
    echo $natom
    sed -i -e "s/geom/$geom/g" ${newfname}
    sed -i -e "s/natom/${natom}/g" $newfname
}

# main section
pydir=~/clones/pyfile
geomdir=~/clones/geom
dirlist=`ls $pydir`
echo $dirlist
skiplist='H2P.py NF86-Di.py NF86-Mo.py NF86-Tet.py NF86-Tri.py'
[ y = y ] && {
    for pydir2 in `ls $pydir`; do
        [ -d "${geomdir}/${pydir2}" ] || mkdir ${geomdir}/${pydir2}
        for filebase in `ls ${pydir}/${pydir2}`; do
            [ ${filebase: -1} = '~' ] && continue
            is_skip=n
            for tmp in ${skiplist}; do
                [ tmp = $filebase ] && is_skip=y
            done
            [ $is_skip = y ] && { echo "${filebase} is skipped"; continue;}
            #filename="${pydir}/${pydir2}/${filename}"
            filename="${pydir}/${pydir2}/${filebase}"
            newfname="${geomdir}/${pydir2}/${filebase//.py/.xyz}"
            echo $filename
            echo $newfname
            orz2xyz $filename $newfname
            #exit 1
        done
    done
}
