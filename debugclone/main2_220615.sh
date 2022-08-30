#!/bin/bash
strpwd=`pwd`
[ "`echo $strpwd | grep 'clones'`" ] && { echo 'Do not employ main2.sh at the "clones" directory';}
source ~/clones/splited/clone_function.sh
RefDir=~kazuma/clones/
#pyroot=~kazuma/clones/pyfile
export pyroot=~kazuma/clones/pyFRgeom
#pydirs=()
#tmps=(pyfile_benzalkane3 pyfile_general pyfile_polyene Cbl)
tmps=(pyfile_benzalkane3 pyfile_general pyfile_polyene TrueCbi)
for tmp in ${tmps[@]}; do
    pydirs="${pydirs[@]} ${pyroot}/${tmp}"
done
chkxroot=~kazuma/clones/chkx
chkx_def2svp="${chkxroot}/chkxfiles ${chkxroot}/chkx_benzalk3_def2svp ${chkxroot}/chkx_cbl_defsvp"
chkx_def2svp_reorder="${chkxroot}/chkx_benzalk3_def2svp_reorder"
chkx_def2tzvp="${chkxroot}/chkx_benzalk3_def2tzvp"
chkx_sto6g="${chkxroot}/chkx_TrueCbi_sto6g"
chkx_sto6g_svp="${chkxroot}/chkx_TrueCbi_sto6g_svp"
chkx_sto6g_tzvpp="${chkxroot}/chkx_TrueCbi_sto6g_tzvpp"
chkx_loc_def2svp="${chkxroot}/chkx_benzalk3_loc_def2svp_reorder"
chkx_sto3g="${chkxroot}/chkx_benzalk3_sto3g"
chkx_sto3g_lowspin="${chkxroot}/chkx_cbl_lowspin_sto3g"
chkx_b3lyp_lowspin="${chkxroot}/chkx_cbl_b3lyp_lowspin"
chkx_b3lyp_sto3g_def2svp_lowspin="${chkxroot}/chkx_low-cbl_b3lyp_sto3g-def2svp"
chkx_reorder_b3lyp_sto3g_def2svp_lowspin="${chkxroot}/chkx_low-cbl_b3lyp_sto3g-def2svp"
chkx_casscf="${chkxroot}/chkx_benzalk3_def2svp_casscf ${chkxroot}/chkx_general_casscf"
chkx_cas_cbl_sto3g_def2svp_PNOCAS="${chkxroot}/chkx_cas-cbl_sto3g_def2svp_bench-for-PNOCAS"
chkx_MScas_cbls_sto6g_tzvpp="${chkxroot}/chkx_MScas_cbls_sto6g_tzvpp"
chkx_MScas2_cbls_sto6g_tzvpp="${chkxroot}/chkx_MScas2_cbls_sto6g_tzvpp"
chkx_MScas3_cbls_svp_tzvpp="${chkxroot}/chkx_MScas3_cbls_svp_tzvpp"
chkx_casscf_sto6g_svp="${chkxroot}/chkx_TrueCbi_casscf_sto6g_svp"
chkx_casscf_sto6g_tzvpp="${chkxroot}/chkx_casscf_sto6g_tzvpp ${chkxroot}/chkx_TrueCbi_casscf_sto6g_tzvpp"
# chkx_testcas might be changed depending on time
chkx_testcas="${chkxroot}/chkx_reorder_MeCblP2_6_7_b3lyp_sto3g-def2svp"
chkx2_def2svp_reorder="${chkxroot}/chkx2_benzalk3_def2svp_reorder"
chkx2_loc_def2svp="${chkxroot}/chkx2_benzalk3_loc_reorder_def2svp"
chkx2_b3lyp_sto3g_def2svp_lowspin="${chkxroot}/chkx2_low-cbl_b3lyp_sto3g-def2svp"
chkx2_locDV_low_cbl_b3lyp_sto3g_def2svp="${chkxroot}/chkx2_locDV_low-cbl_b3lyp_sto3g-def2svp"
chkx2_cbl_mycas2="${chkxroot}/chkx2_mycas2_low-cbl_sto3g-def2svp"
chkx2_cbl_mycasloc1="${chkxroot}/chkx2_mycas-loc1_low-cbl_sto3g-def2svp"

SplDir=~kazuma/clones/splited/
#pydirs=heyhey
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
OrzVer=orz_noGA2
fillnode=n
ncopy=1
OmitOptPos=(0)
usecore=8
valcheck=y
MSorz=n
MS3orz=n
MS5orz=n
temp_orz=n
orzgit2=n
orzmod=n

ischain=n
isdistribute=n
dist_pack=
nchain=1
ndist=1
n_node=1
genechk=n
is_orblocsh=n
loctype=NONE
is_calctest=n

# extrnal options
is_casscf=n
ref_icmr=n
is_nolct=n
is_nolct=n
is_orbloc=n
export is_fullpack=n
names_fullpack=

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
            [ "`echo $opt | grep 'fullpack='`" ] && {
                export is_fullpack=${opt:9}
            }
        done # the end of option modification
        continue
    }

    # opts -> 'ReadInpOpt.sh' -> names
    echo "$ ReadInpOpt -----------------------------------"
    echo ${opts[@]}
    names=(`bash ${SplDir}ReadInpOpt.sh ${opts[@]}`)
    echo ${names[@]}
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'"
        exit 1
    }
    #Loop of generate py and sh file
    Reses=()
    
    # names is list of filenames, which should be generated in one line of option file
    echo "$ NameMod -----------------------------------"
    for Name in "${names[@]}"; do
        opts=(${Name//_/ })
        MolName=${opts[@]:0:1}
        if [ `echo $MolName | grep cbi-` ]; then
            origMol=$MolName
            MolName=${MolName#'cbi-'}
            #Name=${Name#'cbi-'}
            cp ${pyroot}/cbi/$MolName.py $Dir$Name.py
        elif [ `echo $MolName | grep cbl-` ]; then
            origMol=$MolName
            MolName=${MolName#'cbl-'}
            #Name=${Name#'cbl-'}
            cp ${pyroot}/cbl/$MolName.py $Dir$Name.py
        else
            for tmp in ${pydirs}; do
                [ -e "${tmp}/${MolName}.py" ] && tmpdir=${tmp}
            done
            cp ${tmpdir}/$MolName.py $Dir$Name.py
        fi
        
        # pre-modification
        #[ "`echo $Name | grep 'act'`" ] && actmod $Name $Dir
        
        # Modification of python script and omit option
        ResName=
        CountOmit=1
        # opts refers to options of one file
        for opt in ${opts[@]};do
            
            . ~/clones/splited/modopt.sh
            [[ (`printf '%u\n' ${OmitOptPos[@]} | grep -qx "$CountOmit";echo -n $?` -eq 0) || ($opt = chain) || ($opt = moread) ]] || ResName=${ResName}_${opt}
            CountOmit=`expr "$CountOmit" + 1`
        done # the end of opts' loop
        
        #Omit Name option determined by position
        #cp $Dir$Name.py $Dir${Name}_out.py
        #[ $Dir$Name.py != $Dir$MolName$ResName.py ] && {
        #    mv $Dir$Name.py $Dir$MolName$ResName.py
        #    #mv $Dir${Name}_out.py $Dir$MolName${ResName}_out.py
        #}
        #[ -e $Dir$Name.chkx ] && [ $Dir$Name.chkx != $Dir$MolName$ResName.chkx ] && mv $Dir$Name.chkx $Dir$MolName$ResName.chkx
        echo "FullName = $Name"
        #Name=$MolName$ResName
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
        elif [ ${isdistribute} = y ]; then
            dist_pack="${dist_pack} ${Name}"
        elif [ ${is_fullpack} = y ]; then
            :
        else
            #Modification of shell script
            . ${SplDir}modsh.sh
        fi # the end of chain branch
        echo ''
    done # the end of one filename loop

    if [ ${ischain} = y ]; then
        chain_or_dist=Chain
        nindex=$nchain
        . ${SplDir}modsh_chain.sh
    elif [ ${isdistribute} = y ]; then
        :
    elif [ ${is_fullpack} = y ]; then
        tmp=${Reses[@]}
        names_fullpack="${names_fullpack} ${tmp}"
    else
        tmp=${Reses[@]}
        outs=
        for tmp2 in tmp; do
            out="${out} ${tmp2}_out"
        done
        #echo "filename = $tmp"
        sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}qsub.sh
        [ $genechk = y ] && sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}genechk.sh
        [ $is_orblocsh = y ] && sed -i -e "s/filelist=(/filelist=(${tmp} /g" ${Dir}orbloc.sh
    fi
    [ $loctype != NONE ] && cp ${RefDir}orbloc.sh ${Dir}orbloc.sh
    # the end of one line of option file
done < ${RefDir}testinp
if [ ${is_fullpack} = y ]; then
    chain_or_dist=fullpack
    nindex=
    . ${SplDir}modsh_chain.sh
fi

[ $fillnode = y ] && sed -i -e "s/fillnode=n/fillnode=y/g" ${Dir}qsub.sh
sed -i -e "s/usecore=.*/usecore=$usecore/g" ${Dir}qsub.sh
[ ${n_node} -ge 2 ] && [ `expr ${n_node}` ] && sed -i -e "s/n_node=.*/n_node=${n_node}/g" ${Dir}qsub.sh
[ ${isdistribute} = y ] && {
    chain_or_dist=Distribute
    nindex=
    . ${SplDir}modsh_chain.sh
}
echo ""
echo ""
echo "-------------- option list -----------------"
echo "Omit position = ${OmitOptPos[@]}"
echo "OrzVer = ${OrzVer}"
echo "fillnode option is $fillnode"
echo "the number of core = $usecore"
echo "n_node = $n_node"
echo "fullpack option is $is_fullpack"
echo "--------------------------------------------"
echo "Normal termination                          "
