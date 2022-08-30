cp ${RefDir}Base.sh $Dir$Name.sh
sed -i -e "s/JOBNAME=.*/JOBNAME=${Name}/g" ${Dir}${Name}.sh
# PSM version 2 section (If orz is integrated)
#echo "MSorz = ${MSorz}"
            
if [ ${MSorz} = y ]; then
    sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz-MS\/orz-stack/g" $Dir$Name.sh
    sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz-MS\/orz-stack\/obj-opt/g" $Dir$Name.sh
    MSorz=n
elif [ ${MS5orz} = y ]; then
    sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz-MS5\/orz-stack/g" $Dir$Name.sh
    sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz-MS5\/orz-stack\/obj-opt/g" $Dir$Name.sh
    MS5orz=n
elif [ ${temp_orz} = y ]; then
    sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz_temp\/orz/g" $Dir$Name.sh
    sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz_temp\/orz\/obj-opt/g" $Dir$Name.sh
    temp_orz=n
elif [ ${orzgit2} = y ]; then
    sed -i -e "s|ORZSRC=.*|ORZSRC=~kazuma/orzsource/orz-git2/|g" $Dir$Name.sh
    sed -i -e "s|ORZOBJ=.*|ORZOBJ=~kazuma/orzsource/orz-git2/obj-opt|g" $Dir$Name.sh
    orzgit2=n
elif [ ${orzmod} = y ]; then
    sed -i -e "s|ORZSRC=.*|ORZSRC=~kazuma/orzsource/orz-mod/|g" $Dir$Name.sh
    sed -i -e "s|ORZOBJ=.*|ORZOBJ=~kazuma/orzsource/orz-mod/obj-opt2|g" $Dir$Name.sh
    orzmod=n
else
    echo "default orz setting is used"
    #sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/${OrzVer}\/orz-stack/g" $Dir$Name.sh
    #sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/${OrzVer}\/orz-stack\/obj-opt/g" $Dir$Name.sh
fi
[ $ref_icmr = y ] && {
    sed -i -e "s/lct/icmr/g" $Dir$Name.sh
    ref_icmr=n
    #echo 'lct -> icmr'
}
[ $is_casscf = y ] && {
    sed -i -e "s/#casscf#//g" $Dir$Name.sh
    is_casscf=n
    #echo 'turn on casscf option'
}
[ $is_nolct = y ] && {
    sed -i -e 's|`eval echo $MPIRUNQ` $ORZOBJ/src/sci/lct/lct|#`eval echo $MPIRUNQ` $ORZOBJ/src/sci/lct/lct|g' $Dir$Name.sh
    is_nolct=n
    #echo 'lct -> #lct'
            }

if [ $loctype = NONE ]; then
    :
elif [ $loctype = DV ]; then
    sed -i -e 's/loctype=NONE/loctype=DV/g' $Dir$Name.sh
elif [ $loctype = CA ]; then
    sed -i -e 's/loctype=NONE/loctype=CA/g' $Dir$Name.sh
elif [ $loctype = nC ]; then
    sed -i -e 's/loctype=NONE/loctype=nC/g' $Dir$Name.sh
fi
