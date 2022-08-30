RefDir=~kazuma/clones/
PyDir=~kazuma/clones/pyfiles/
chkxDir=~kazuma/clones/chkxfiles/
SplDir=~kazuma/clones/splited/
#variable
Dir=./
OrzVer=saitow-orz3
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
            [ "`echo $opt | grep 'fillnode'`" ] && fillnode=y
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
    
    count=0
    # read one molecule options
    for opt in ${opts[@]}; do
        # check whether molecule original python script in clone directory
        [ "$count" -eq 0 ] && {
            MolName="$opt";         
            names=($MolName)
            [ -e "${PyDir}${MolName}.py" ] || { echo "${MolName}.py could not be found."; exit 1; }
            count=`expr "$count" + 1`
            continue;
        }
        #Form name of ImplType
        [ "`echo $opt | grep 'hint.ImplTypePM'`" ] && {
            case $opt in
                hint.ImplTypePM)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp1=${tmp}_incore
                        tmp2=${tmp}_MS
                        names=("${names[@]}" $tmp1 $tmp2)
                    done ;;
                hint.ImplTypePM=incore)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp1=${tmp}_incore
                        names=("${names[@]}" $tmp1)
                    done ;;
                hint.ImplTypePM=MS)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp1=${tmp}_MS
                        names=("${names[@]}" $tmp1)
                    done ;;
            esac
        }
        #Form name of isOnTheFly
        [ "`echo $opt | grep 'hint.isOnTheFly'`" ] && {
            case $opt in
                hint.isOnTheFly)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp1=${tmp}_NotOn
                        tmp2=${tmp}_On
                        names=("${names[@]}" $tmp1 $tmp2)
                    done ;;
                hint.isOnTheFly=On)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp2=${tmp}_On
                        names=("${names[@]}" $tmp2)
                    done ;;
                hint.isOnTheFly=Not)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp2=${tmp}_NotOn
                        names=("${names[@]}" $tmp2)
                    done ;;
            esac
        }
        #Form name of ChargeType
        [ "`echo $opt | grep 'hint.ChargeType'`" ] && {
            case $opt in
                hint.ChargeType)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp1=${tmp}_Mull
                        tmp2=${tmp}_Low
                        names=("${names[@]}" $tmp1 $tmp2)
                    done ;;
                hint.ChargeType=Mull)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp2=${tmp}_Mull
                        names=("${names[@]}" $tmp2)
                    done ;;
                hint.ChargeType=Low)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp2=${tmp}_Low
                        names=("${names[@]}" $tmp2)
                    done ;;
            esac
        }
        #Form name of Thresh of jacobi
        [ "`echo $opt | grep 'Tj'`" ] && {
            tmpj=${opt:3}
            IFSBACK=$IFS
            IFS=,
            tmpsj=(${tmpj})
            IFS=$IFSBACK
            tmps=(${names[@]})
            names=()
            for tmp in "${tmps[@]}"; do
                for tmpj in ${tmpsj[@]}; do
                    tmp1=${tmp}_Tj${tmpj}
                    names=("${names[@]}" $tmp1)
                done
            done
        }
        #Form name of Thresh of NR macro iterarion
        [ "`echo $opt | grep 'Tl'`" ] && {
            tmpl=${opt:3}
            IFSBACK=$IFS
            IFS=,
            tmpsl=(${tmpl})
            IFS=$IFSBACK
            tmps=(${names[@]})
            names=()
            for tmp in "${tmps[@]}"; do
                for tmpl in ${tmpsl[@]}; do
                    tmp1=${tmp}_Tl${tmpl}
                    names=("${names[@]}" $tmp1)
                done
            done
        }
        #Form name of Thresh of davidson iteration
        [ "`echo $opt | grep 'Tr'`" ] && {
            tmpr=${opt:3}
            IFSBACK=$IFS
            IFS=,
            tmpsr=(${tmpr})
            IFS=$IFSBACK
            tmps=(${names[@]})
            names=()
            for tmp in "${tmps[@]}"; do
                for tmpr in ${tmpsr[@]}; do
                    tmp1=${tmp}_Tr${tmpr}
                    names=("${names[@]}" $tmp1)
                done
            done
        }
        #Form name of molecule basis
        [ "`echo $opt | grep 'Mbasis'`" ] && {
            case $opt in
                Mbasis=def2-SVP)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp1=${tmp}_def2svp
                        names=("${names[@]}" $tmp1)
                    done ;;
                Nbasis=def2-TZVPP)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp2=${tmp}_def2tzvpp
                        names=("${names[@]}" $tmp2)
                    done ;;
                Mbasis=cc-pvdz)
                    tmps=(${names[@]})
                    names=()
                    for tmp in "${tmps[@]}"; do
                        tmp2=${tmp}_ccpvdz
                        names=("${names[@]}" $tmp2)
                    done ;;
            esac
        }
        #Form name of moread
        [ "`echo $opt | grep 'moread'`" ] && {
            [ -e "${chkxDir}${MolName}.chkx" ] || { echo "${MolName}.chkx could not be found."; exit 1; }
            tmps=(${names[@]})
            names=()
            for tmp in "${tmps[@]}"; do
                tmp2=${tmp}_moread
                names=("${names[@]}" $tmp2)
            done
        }
        #Form name of maxloop0
        [ "`echo $opt | grep 'maxloop0'`" ] && {
            tmps=(${names[@]})
            names=()
            for tmp in "${tmps[@]}"; do
                tmp2=${tmp}_maxloop0
                names=("${names[@]}" $tmp2)
            done
        }
        count=`expr "$count" + 1`
    done
    
    #Loop of generate py and sh file
    Reses=()
    for Name in "${names[@]}"; do
        cp $PyDir$MolName.py $Dir$Name.py
        opts=(${Name//_/ })
        
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

