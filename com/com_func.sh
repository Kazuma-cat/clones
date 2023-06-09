#!/bin/bash
geomdet(){
    geomname=$1
    geompath=$geomroot/${geomname//'-'/'/'}.xyz
    if [ -f $geompath ];then
        echo $geompath
    else ls $geompath
    fi
    #geom-name
}
