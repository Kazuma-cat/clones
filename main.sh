RefDir=~kazuma/clones/
#pyroot=~kazuma/clones/pyfile
pyroot=~kazuma/clones/pyFRgeom
#pydirs=()
#tmps=(pf_benzalkane2 pyfile_benzalkane pyfile_general)
tmps=(pf_benzalkane2 pyfile_general)
for tmp in ${tmps[@]}; do
    pydirs="${pydirs[@]} ${pyroot}/${tmp}"
done
chkxroot=~kazuma/clones/chkx
chkxdirs=()
chkx_def2svp=()
chkx_sto3g=()
tmps_def2svp=(chkxfiles chkx_benzalkane_reorder chkx_benzalk_sto-3g)
for tmp in ${tmps[@]}; do
    chkxdirs="${chkxdirs[@]} ${chkxroot}/${tmp}"
done
def2svps=(chkxfiles chkx_benzalk2_reorder_dev2svp)
for tmp in ${def2svps[@]}; do
    chkx_def2svp="${chkx_def2svp[@]} ${chkxroot}/${tmp}"
done
loc_def2svps=(chkx_benzalk2_loc_reorder_dev2svp)
for tmp in ${loc_def2svps[@]}; do
    chkx_loc_def2svp="${chkx_loc_def2svp[@]} ${chkxroot}/${tmp}"
done
sto3gs=(chkx_benzalk2_sto-3g)
for tmp in ${sto3gs[@]}; do
    chkx_sto3g="${chkx_sto3g[@]} ${chkxroot}/${tmp}"
done
tmp_casscf=(chkx_benzalk2_casscf)
for tmp in ${tmp_casscf[@]}; do
    chkx_casscf="${chkx_casscf[@]} ${chkxroot}/${tmp}"
done
SplDir=~kazuma/clones/splited/
#pydirs=heyhey
echo ${pydirs}
export pydirs
export PyDir1
export PyDir2
export RefDir
export chkxDir
export chkx_def2svp
export chkx_sto3g
export SplDir
# optional variable
Dir=./
#OrzVer=saitow-orz_temp
OrzVer=saitow-orz-MS5
fillnode=n
ncopy=1
OmitOptPos=(0)
usecore=8
valcheck=y
MSorz=n
MS3orz=n
temp_orz=n
ischain=n
nchain=1
n_node=1
genechk=n
is_orblocsh=n

# extrnal options
is_casscf=n
ref_icmr=n
is_nolct=n
is_nolct=n
is_orbloc=n

#beggining of cloneing orz inputs
cp ${RefDir}qsub.sh $Dir
chmod +x ${Dir}qsub.sh
while read -a opts; do
    [ -z ${opts} ] && continue
    [ "`echo ${opts[@]} | grep '!!'`" ] && continue
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
            [ "`echo $opt | grep 'n_node='`" ] && n_node=${opt:7}
            [ "`echo $opt | grep 'genechk='`" ] && {
                genechk=${opt:8}
                [ ${genechk} = y ] && {
                    cp ${RefDir}genechk.sh $Dir
                    chmod +x ${Dir}genechk.sh
                }
            }
            [ "`echo $opt | grep 'is_orblocsh='`" ] && {
                is_orblocsh=${opt:12}
                [ ${is_orblocsh} = y ] && {
                    cp ${RefDir}orbloc.sh $Dir
                    chmod +x ${Dir}orbloc.sh
                }
            }
        done # the end of option modification
        continue
    }

    # opts -> 'ReadInpOpt.sh' -> names
    names=(`bash ${SplDir}ReadInpOpt.sh ${opts[@]}`)
    echo ${names[@]}
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'"
        exit 1
    }
    #Loop of generate py and sh file
    Reses=()
    # names is list of filenames, which should be generated in one line of option file
    for Name in "${names[@]}"; do
        opts=(${Name//_/ })
        MolName=${opts[@]:0:1}
        for tmp in ${pydirs}; do
            [ -e "${tmp}/${MolName}.py" ] && tmpdir=${tmp}
        done
        cp ${tmpdir}/$MolName.py $Dir$Name.py
        
        # pre-modification
        if [ "`echo $Name | grep 'act'`" ];then
            active=`echo $Name | grep -o 'act[0-9]\+'`
            echo $active
            active=${active:3}
            IFSBACK=$IFS
            IFS='-'
            tmps=("${active}")
            IFS=$IFSBACK
            active_occ=${tmps[0]}
            active_vir=${tmps[1]}
            closed=`grep 'icmr.closed' $Dir$Name.py | grep -o '[0-9]\+'`
            occ=`grep 'icmr.occ' $Dir$Name.py | grep -o '[0-9]\+'`
            echo $active_occ
            echo $active_vir
            echo $closed
            echo $occ
            closed=`expr $closed + $occ - $active_occ`
            active=`expr $active_occ + $active_vir`
            echo $closed
            echo $active
            sed -i -e "s/icmr.closed\s*=.*/icmr.closed = \[$closed\]/g" $Dir$Name.py 
            sed -i -e "s/icmr.occ\s*=.*/icmr.occ = \[$active\]/g" $Dir$Name.py 
        fi
        # Modification of python script and omit option
        ResName=
        CountOmit=1
        # opts refers to options of one file
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
                PM)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PM\"/g' $Dir$Name.py ;;
                PMNR)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PMNR\"/g' $Dir$Name.py ;;
                PMNR-nJ)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PMNR-nJ\"/g' $Dir$Name.py ;;
                PSM1)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
                    sed -i -e 's/lct.LocPower =.*/lct.LocPower = 1/g' $Dir$Name.py ;;
                PSM2)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
                    sed -i -e 's/lct.LocPower =.*/lct.LocPower = 2/g' $Dir$Name.py ;;
                PSM1Ver2)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
                    sed -i -e 's/lct.LocPower =.*/lct.LocPower = 1/g' $Dir$Name.py
                    sed -i -e 's/#hint.PSMVersion =.*/hint.PSMVersion = 2/g' $Dir$Name.py
                    sed -i -e "s/# lct.UseVM12     = False/# lct.UseVM12     = False\nlct.UseJacobiGuess = True/g" $Dir$Name.py
                    # comment out PMNR option
                    sed -i -e 's/hint.isOnTheFly/#hint.isOnTheFly/g' $Dir$Name.py
                    sed -i -e 's/hint.ImplTypePM/#hint.ImplTypePM/g' $Dir$Name.py
                    sed -i -e 's/hint.ChargeType/#hint.ChargeType/g' $Dir$Name.py
                    sed -i -e 's/hint.PMNRdebug/#hint.PMNRdebug/g' $Dir$Name.py
                    sed -i -e 's/hint.kscal/#hint.kscal/g' $Dir$Name.py
                
                    MSorz=y;;
                PSM2Ver2)
                    sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
                    sed -i -e 's/#hint.PSMVersion =.*/hint.PSMVersion = 2/g' $Dir$Name.py
                    sed -i -e 's/#UseJacobiGuess/UseJacobiGuess/g' $Dir$Name.py
                    # comment out PMNR option
                    sed -i -e 's/hint.isOnTheFly/#hint.isOnTheFly/g' $Dir$Name.py
                    sed -i -e 's/hint.ImplTypePM/#hint.ImplTypePM/g' $Dir$Name.py
                    sed -i -e 's/hint.ChargeType/#hint.ChargeType/g' $Dir$Name.py
                    sed -i -e 's/hint.PMNRdebug/#hint.PMNRdebug/g' $Dir$Name.py
                    sed -i -e 's/hint.kscal/#hint.kscal/g' $Dir$Name.py
                
                    MSorz=y;;
                MS3orz)
                    sed -i -e 's/lct.test.*/#lct.test = False/g' $Dir$Name.py
                    sed -i -e 's/lct.DoPNO.*/#lct.DoPNO = True/g' $Dir$Name.py
                    sed -i -e 's/lct.UseOrthPNOs.*/#lct.UseOrthPNOs = True/g' $Dir$Name.py
                    sed -i -e 's/lct.RIMP2.*/#lct.RIMP2 = False/g' $Dir$Name.py
                    MS3orz=y;;
                PAOs)
                    sed -i -e 's/lct.UsePAOs =.*/lct.UsePAOs = True/g' $Dir$Name.py
                    sed -i -e 's/lct.FormLVOs =.*/lct.FormLVOs = False/g' $Dir$Name.py ;;
                casscf)
                    is_casscf=y ;;
                no_lct)
                    is_nolct=y ;;
                CMO)
                    sed -i -e 's/lct.DoLoc.*/lct.DoLoc = False/g' $Dir$Name.py ;;
                Ref)
                    if [ "`grep 'icmr.occ' $Dir$Name.py`" ]; then
                        if [ `grep 'icmr.occ' $Dir$Name.py | grep -o '[0-9]\+'` -eq 0 ]; then
                            sed -i -e 's/lct.RIMP2\s*=.*/lct.RIMP2 = True/g' $Dir$Name.py
                        else
                            echo 'turn on icmr option'
                            ref_icmr=y
                        fi
                    else
                        sed -i -e 's/lct.RIMP2\s*=.*/lct.RIMP2 = True/g' $Dir$Name.py
                    fi ;;
                moreadonly)
                    sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py;;
                moread-def2svp)
                    sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
                    tmpchk=n
                    for tmp in ${chkx_def2svp[@]}; do
                        [ -e "${tmp}/${MolName}.chkx" ] && {
                            cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                            tmpchk=y
                        }
                    done
                    [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
                moread-loc-def2svp)
                    sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
                    tmpchk=n
                    for tmp in ${chkx_loc_def2svp[@]}; do
                        [ -e "${tmp}/${MolName}.chkx" ] && {
                            cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                            tmpchk=y
                        }
                    done
                    [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
                moread-sto3g)
                    sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
                    tmpchk=n
                    for tmp in ${chkx_sto3g[@]}; do
                        [ -e "${tmp}/${MolName}.chkx" ] && {
                            cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                            tmpchk=y
                        }
                    done
                    [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
                moread-casscf)
                    sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
                    tmpchk=n
                    for tmp in ${chkx_casscf[@]}; do
                        [ -e "${tmp}/${MolName}.chkx" ] && {
                            cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                            tmpchk=y
                        }
                    done
                    [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
                maxloop0)
                    sed -i -e 's/scf.maxloop =.*/scf.maxloop = 0/g' $Dir$Name.py ;;
                chain)
                    ischain=y ;;
                nolct)
                    is_nolct=y ;;
                orbloc)
                    is_orbloc=y ;;
                def2svp)
                    sed -i -e 's/qatom.basis.*/qatom.basis = baslib("def2-SVP")/g # Molecule Basis Set' $Dir$Name.py ;;
                def2tzvpp)
                    sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("def2-TZVPP") # Molecule Basis Set/g' $Dir$Name.py ;; 
                    
                ccpvdz)
                    sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("cc-pvdz") # Molecule Basis Set/g' $Dir$Name.py ;;
                sto-3g)
                    sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("sto-3g") # Molecule Basis Set/g' $Dir$Name.py ;;
                *)
                    if [ "`echo $opt | grep 'Tj'`" ];then
                        tmpj=${opt:2}
                        sed -i -e "s/hint.jacobi_thresh.*/hint.jacobi_thresh = ${tmpj}/g" $Dir$Name.py
                    elif [ "`echo $opt | grep 'Tl'`" ];then
                        tmpl=${opt:2}
                        sed -i -e "s/hint.loc_thresh.*/hint.loc_thresh = ${tmpl}/g" $Dir$Name.py
                    elif [ "`echo $opt | grep 'Tr'`" ];then
                        tmpr=${opt:2}
                        sed -i -e "s/hint.kscal.*/hint.kscal = ${tmpr}/g" $Dir$Name.py
                    elif [ "`echo $opt | grep 'TCutPNOrho0'`" ];then
                        tmpr=${opt:11}
                        sed -i -e "s/lct.TCutPNOrho0.*/lct.TCutPNOrho0 = ${tmpr}/g" $Dir$Name.py
                    elif [ "`echo $opt | grep 'TCutPairs'`" ];then
                        tmpr=${opt:9}
                        sed -i -e "s/lct.TCutPairs.*/lct.TCutPairs = ${tmpr}/g" $Dir$Name.py
                    elif [ "`echo $opt | grep 'TCutPre'`" ];then
                        tmpr=${opt:7}
                        sed -i -e "s/lct.TCutPre.*/lct.TCutPre = ${tmpr}/g" $Dir$Name.py
                    else
                        echo "Pyfile Modification Error: ${opt} option is not defined"
                    fi
            esac # end of opt modification
            
            #[[ (`printf '%u\n' ${OmitOptPos[@]} | grep -qx "$CountOmit";echo -n $?` -eq 0) || ($opt = chain) || ($opt = moread) || ($opt = maxloop0) ]] || ResName=${ResName}_${opt}
            [[ (`printf '%u\n' ${OmitOptPos[@]} | grep -qx "$CountOmit";echo -n $?` -eq 0) || ($opt = chain) || ($opt = moread) ]] || ResName=${ResName}_${opt}
            CountOmit=`expr "$CountOmit" + 1`
        done # the end of opts' loop
        
        #Omit Name option determined by position
        [ $Dir$Name.py != $Dir$MolName$ResName.py ] && mv $Dir$Name.py $Dir$MolName$ResName.py
        [ -e $Dir$Name.chkx ] && mv $Dir$Name.chkx $Dir$MolName$ResName.chkx
        echo "FullName = $Name"
        Name=$MolName$ResName
        Reses=(${Reses[@]} $Name)
        
        #clone option
        if [ ${ischain} = y ]; then
            # source orz check
            if [ -z ${source_check} ]; then
                source_check=${MSorz}
            else
                [ ${source_check} = ${MSorz} ] || {
                    echo 'Chain Error: orz source must be the same in one chain option'
                    exit 1
                }
            fi
        else
            if [ $ncopy -ge 2 ]; then
                i=1
                
                while [ $i -le $ncopy ]; do
                    cp $Dir$Name.py ${Dir}${Name}_${i}.py
                    i=`expr "$i" + 1`
                done
                cp ${RefDir}CBase.sh $Dir$Name.sh
                sed -i -e "s/MOLNAME=/MOLNAME=${Name}/g" ${Dir}${Name}.sh
                sed -i -e "s/ncopy=/ncopy=${ncopy}/g" ${Dir}${Name}.sh
                
            elif [ $ncopy -eq 1 ]; then
                #Modification of shell script
                cp ${RefDir}Base.sh $Dir$Name.sh
                sed -i -e "s/JOBNAME=.*/JOBNAME=${Name}/g" ${Dir}${Name}.sh
                # PSM version 2 section (If orz is integrated)
                #echo "MSorz = ${MSorz}"
                
                if [ ${MSorz} = y ]; then
                    sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz-MS\/orz-stack/g" $Dir$Name.sh
                    sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz-MS\/orz-stack\/obj-opt/g" $Dir$Name.sh
                    MSorz=n
                elif [ ${MS3orz} = y ]; then
                    sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz-MS3\/orz-stack/g" $Dir$Name.sh
                    sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz-MS3\/orz-stack\/obj-opt/g" $Dir$Name.sh
                    MS3orz=n
                elif [ ${temp_orz} = y ]; then
                    sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz_temp\/orz/g" $Dir$Name.sh
                    sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz_temp\/orz\/obj-opt/g" $Dir$Name.sh
                    temp_orz=n
                else
                    sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/${OrzVer}\/orz-stack/g" $Dir$Name.sh
                    sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/${OrzVer}\/orz-stack\/obj-opt/g" $Dir$Name.sh
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
                [ $is_orbloc = y ] && {
                    sed -i -e 's/orbloc=n/orbloc=y/g' $Dir$Name.sh
                    is_orbloc=n
                }
            fi # the end of ncopy(coming soon)
        fi # the end of chain branch
    done # the end of one filename loop

    if [ ${ischain} = y ]; then
        cp ${RefDir}ChainBase.sh ${Dir}Chain${nchain}.sh
        tmp=${Reses[@]}
        sed -i -e "s/JOBNAMES=.*/JOBNAMES=(${tmp})/g" ${Dir}Chain${nchain}.sh
        if [ ${MSorz} = y ]; then
            sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz-MS\/orz-stack/g" ${Dir}Chain${nchain}.sh
            sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz-MS\/orz-stack\/obj-opt/g" ${Dir}Chain${nchain}.sh
            MSorz=n
        elif [ ${MS3orz} = y ]; then
            sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz-MS3\/orz-stack/g" ${Dir}Chain${nchain}.sh
            sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz-MS3\/orz-stack\/obj-opt/g" ${Dir}Chain${nchain}.sh
            MS3orz=n
        elif [ ${temp_orz} = y ]; then
            sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/saitow-orz_temp\/orz/g" ${Dir}Chain${nchain}.sh
            sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/saitow-orz_temp\/orz\/obj-opt/g" ${Dir}Chain${nchain}.sh
            temp_orz=n
        else
            sed -i -e "s/ORZSRC=.*/ORZSRC=~kazuma\/${OrzVer}\/orz-stack/g" ${Dir}Chain${nchain}.sh
            sed -i -e "s/ORZOBJ=.*/ORZOBJ=~kazuma\/${OrzVer}\/orz-stack\/obj-opt/g" ${Dir}Chain${nchain}.sh
        fi
        [ $ref_icmr = y ] && {
            sed -i -e "s/lct/icmr/g" ${Dir}Chain${nchain}.sh
            ref_icmr=n
            #echo 'lct -> icmr'
        }
        [ $is_casscf = y ] && {
            sed -i -e "s/#casscf#//g" ${Dir}Chain${nchain}.sh
            is_casscf=n
            echo 'turn on casscf option'
        }
        [ $is_nolct = y ] && {
            sed -i -e 's|`eval echo $MPIRUNQ` $ORZOBJ/src/sci/lct/lct|#`eval echo $MPIRUNQ` $ORZOBJ/src/sci/lct/lct|g' ${Dir}Chain${nchain}.sh
            is_nolct=n
            #echo 'lct -> #lct'
        }
        [ ${is_orbloc} = y ] && {
            sed -i -e 's/orbloc=n/orbloc=y/g' ${Dir}Chain${nchain}.sh
            is_orbloc=n
        }
        
        sed -i -e "s/filelist=(/filelist=(Chain${nchain} /g" ${Dir}qsub.sh
        [ $genechk = y ] && sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}genechk.sh
        [ $is_orblocsh = y ] && sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}orbloc.sh
        nchain=`expr ${nchain} + 1`
        unset source_check
        ischain=n
    else
        tmp=${Reses[@]}
        #echo "filename = $tmp"
        sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}qsub.sh
        [ $genechk = y ] && sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}genechk.sh
        [ $is_orblocsh = y ] && sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}orbloc.sh
    fi
    # the end of one line of option file
done < ${RefDir}testinp
echo "Omit position = ${OmitOptPos[@]}"
echo "fillnode option is $fillnode"
[ $fillnode = y ] && sed -i -e "s/fillnode=n/fillnode=y/g" ${Dir}qsub.sh
echo "the number of core = $usecore"
sed -i -e "s/usecore=.*/usecore=$usecore/g" ${Dir}qsub.sh
echo "n_node = $n_node"
[ ${n_node} -ge 2 ] && [ `expr ${n_node}` ] && sed -i -e "s/n_node=.*/n_node=${n_node}/g" ${Dir}qsub.sh


