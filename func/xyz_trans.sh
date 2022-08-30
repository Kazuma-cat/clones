#!/bin/bash
filepath=$1
refpoint=()
while read -a line; do
    [ $Nline -eq 0 ] && { Nline=`expr $Nline + 1`;continue;}
    [ $Nline -eq 1 ] && { Nline=`expr $Nline + 1`;continue;}
    [ -z $line ] && break
    [ ${#line[@]} != 4 ] && { echo ${#line[@]};Nline=`expr $Nline + 1`;continue;}
    if [ x${line[0]} = xCo ]; then
        refpoint=(${line[1]} ${line[2]} ${line[3]})
        break
    fi
done < $filepath
geom=
while read -a line; do
    if [ ${#line[@]} != 4 ]; then
        geom="$geom$line\n"
    else
        python3 -c "print(${line[1]}-${refpoint[0]})"
        x=`python3 -c "print(${line[1]}-${refpoint[0]})"`
        y=`python3 -c "print(${line[2]}-${refpoint[1]})"`
        z=`python3 -c "print(${line[3]}-${refpoint[2]})"`
        geom="$geom${line[0]} $x $y $z\n"
    fi
done < $filepath
echo $geom
