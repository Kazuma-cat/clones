RefDir=~kazuma/clones/
PyDir=~kazuma/clones/pyfiles/
chkxDir=~kazuma/clones/chkxfiles/
SplDir=~kazuma/clones/splited/
export PyDir
export RefDir
export chkxDir
export SplDir
#variable
Dir=./
OrzVer=saitow-orz_temp
fillnode=n
ncopy=1
OmitOptPos=(0)
usecore=8
valcheck=y
#beggining of cloneing orz inputs
cp ${RefDir}qsub.sh $Dir
while read -a opts; do
    [ "`echo ${opts[@]} | grep '!!'`" ] && continue;
    # get options
    [ "`echo ${opts[@]} | grep '!'`" ] && {
        for opt in ${opts[@]}; do
            [ "`echo $opt | grep 'Dir='`" ] && Dir=${opt:3}
            [ "`echo $opt | grep 'OrzVer='`" ] && OrzVer=${opt:7}
            [ "`echo $opt | grep 'fillnode=y'`" ] && fillnode=y
            [ "`echo $opt | grep 'ncopy='`" ] && ncopy=${opt:6}
            [ "`echo $opt | grep 'OmitOptPos='`" ] && {
                OmitOptPos=${opt:11}
                OmitOptPos=(${OmitOptPos//,/ })
            }
            [ "`echo $opt | grep 'usecore='`" ] && usecore=${opt:8}
        done
        continue
    }
    #check option values
    [ $valcheck = y ] && {
        printenv Dir
        printenv OrzVar
        printenv fillnode
        printenv ncopy
        valcheck=n
    }
    echo "opts = ${opts[@]}"
    names=(`bash ${SplDir}ReadInpOpt.sh ${opts[@]}`)
    echo "names = ${names[@]}"
    [ "`echo ${names[@]} | grep 'Error'`" ] && exit 1
    #Loop of generate py and sh file
    Reses=()
    for Name in "${names[@]}"; do
        opts=(${Name//_/ })
        MolName=${opts[@]:0:1}
        cp $PyDir$MolName.py $Dir$Name.py
        #Modification of python script and omit option
        ResName=
        CountOmit=1
        for opt in ${opts[@]};do
            case $opt in
                $MolName)
                    CountOmit=`expr "$CountOmit" + 1`
                    continue;;
                MS)
                    sed -i -e 's/hint.ImplTypePM =.*/hint.ImplTypePM = "MS"/g' $Dir$Name.py ;;
                incore)
                    sed -i -e 's/hint.ImplTypePM =.*/hint.ImplTypePM = \"incore\"/g' $Dir$Name.py ;;
                On)
                    sed -i -e 's/hint.isOnTheFly =.*/hint.isOnTheFly = True/g' $Dir$Name.py ;;
                NotOn)
                    sed -i -e 's/hint.isOnTheFly =.*/hint.isOnTheFly = False/g' $Dir$Name.py ;;
                Mull)
                    sed -i -e 's/hint.ChargeType =.*/hint.ChargeType = \"Mulliken\"/g' $Dir$Name.py ;;
                Low)
                    sed -i -e 's/hint.ChargeType =.*/hint.ChargeType = \"Loewdin\"/g' $Dir$Name.py ;;
                PMNR)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PMNR\"/g' $Dir$Name.py ;;
                PSM)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py ;;
                PSMVer2)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
                    sed -i -e 's/#hint.PSMVersion =.*/hint.PSMVersion = 2/g' $Dir$Name.py ;;
                moread)
                    sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
                    cp $chkxDir$MolName.chkx $Dir$Name.chkx;;
                maxloop0)
                    sed -i -e 's/#scf.maxloop = 0/scf.maxloop = 0/g' $Dir$Name.py ;;
                # !!!! under construction !!!!
                def2svp)
                    sed -i -e 's/hint.isOnTheFly =.*/hint.isOnTheFly = False/g' $Dir$Name.py ;;
                def2tzvpp)
                    sed -i -e 's/hint.ChargeType =.*/hint.ChargeType = Mull/g' $Dir$Name.py ;;
                ccpvdz)
                    sed -i -e 's/hint.ChargeType =.*/hint.ChargeType = Low/g' $Dir$Name.py ;;
                *)
                    if [ "`echo $opt | grep 'Tj'`" ];then
                        tmpj=${opt:2}
                        sed -i -e "s/hint.jacobi_thresh.*/hint.jacobi_thresh = ${tmpj}/g" $Dir$Name.py
                    elif [ "`echo $opt | grep 'Tl'`" ];then
                        tmpl=${opt:2}
                        sed -i -e "s/hint.loc_thresh.*/hint.loc_thresh = ${tmpl}/g" $Dir$Name.py
                    elif [ "`echo $opt | grep 'Tr'`" ];then
                        tmpr=${opt:2}
                        sed -i -e "s/hint.res_tol.*/hint.res_tol = ${tmpr}/g" $Dir$Name.py
                    else
                        echo "Pyfile Modification Error: ${opt} option is not defined"
                    fi
            esac
            [[ (`printf '%u\n' ${OmitOptPos[@]} | grep -qx "$CountOmit";echo -n $?` -eq 0) || ($opt = moread) || ($opt = maxloop0) ]] || ResName=${ResName}_${opt}
            CountOmit=`expr "$CountOmit" + 1`
        done
        #Omit Name option determined by position
        mv $Dir$Name.py $Dir$MolName$ResName.py
        [ -e $Dir$Name.chkx ] && mv $Dir$Name.chkx $Dir$MolName$ResName.chkx
        echo "FullName = $Name"
        Name=$MolName$ResName
        Reses=(${Reses[@]} $Name)
        #clone option
        if [ $ncopy -ge 2 ]; then
            i=1
            while [ $i -le $ncopy ]; do
                cp $Dir$Name.py ${Dir}${Name}_${i}.py
                i=`expr "$i" + 1`
            done
            cp ${RefDir}CBase.sh $Dir$Name.sh
            sed -i -e "s/MOLNAME=/MOLNAME=${Name}/g" ${Dir}${Name}.sh
            sed -i -e "s/ncopy=/ncopy=${ncopy}/g" ${Dir}${Name}.sh
            sed -i -e "s/ORZSRC=/ORZSRC=~kazuma\/${OrzVer}\/orz/g" $Dir$Name.sh
            sed -i -e "s/ORZOBJ=/ORZOBJ=~kazuma\/${OrzVer}\/orz\/obj-opt/g" $Dir$Name.sh
        elif [ $ncopy -eq 1 ]; then
            #Modification of shell script
            cp ${RefDir}Base.sh $Dir$Name.sh
            sed -i -e "s/JOBNAME=/JOBNAME=${Name}/g" ${Dir}${Name}.sh
            sed -i -e "s/ORZSRC=/ORZSRC=~kazuma\/${OrzVer}\/orz/g" $Dir$Name.sh
            sed -i -e "s/ORZOBJ=/ORZOBJ=~kazuma\/${OrzVer}\/orz\/obj-opt/g" $Dir$Name.sh
        fi
    done
    tmp=${Reses[@]}
    echo "filename = $tmp"
    sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}qsub.sh
done < ${RefDir}testinp
echo "Omit position = ${OmitOptPos[@]}"
echo "fillnode option is $fillnode"
[ $fillnode = y ] && sed -i -e "s/fillnode=n/fillnode=y/g" ${Dir}qsub.sh
echo "the number of core = $usecore"
sed -i -e "s/usecore=.*/usecore=$usecore/g" ${Dir}qsub.sh

