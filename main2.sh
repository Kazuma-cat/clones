#!/bin/bash
[ "`pwd | grep 'clones'`" ] && { echo 'Do not employ main2.sh at the "clones" directory';exit 1;}
#RefDir=~kazuma/clones/
#SplDir=~kazuma/clones/splited/
#export pyroot=~kazuma/clones/pyFRgeom
##chkxroot=~kazuma/clones/chkx
#chkxroot=~kazuma/clones/chkx2
# setting -------------------------------
. ~/clones/splited/clone_function.sh #.
. ~/clones/splited/dir_setting.sh #.
. ~/clones/splited/arg_setting.sh #.
. ~/clones/com/com_func.sh #.
export pydirs
export PyDir1
export PyDir2
export RefDir
export chkxDir
export chkx_def2svp
export chkx_sto3g
export SplDir
# ---------------------------------------


# main prcess -------------------------------------------------
cp ${RefDir}qsub.sh $Dir
chmod +x ${Dir}qsub.sh
while read -a opts; do
    [ -z ${opts} ] && continue
    #[ "`echo ${opts[@]} | grep '!!'`" ] && continue
    [ ${opts:0:1} != '@' ] && continue
    # get options ------------------------------------------------
    #[ "`echo ${opts[@]} | grep '!'`" ] && {
    [ ${opts:0:2} = '@@' ] && {
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
    opts[0]=${opts[0]:1}
    echo ${opts[@]}
    # opts -> 'ReadInpOpt.sh' -> names ------------------------------------------------------
    echo "$ option processing -----------------------------------"
    #echo "#row option#       : ${opts[@]}"
    #bash ${SplDir}ReadInpOpt.sh ${opts[@]}
    #exit 1
    names=(`bash ${SplDir}ReadInpOpt.sh ${opts[@]}`) #.
    echo "#processed option# : ${names[@]}"
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'"
        exit 1
    }
    Reses=()
    
    # pyfile generaion -----------------------------------------------------------------------
    echo "$ pyfile generation -----------------------------------"
    for Name in "${names[@]}"; do
        opts=(${Name//_/ })
        MolName=${opts[@]:0:1}
        origmolname=${opts[@]:0:1}
        cp ${RefDir}/pybase.py $Dir$Name.py
        geom2py $MolName $Dir$Name.py
        #if [ `echo $MolName | grep cbi-` ]; then
        #    origMol=$MolName
        #    MolName=${MolName#'cbi-'}
        #    #Name=${Name#'cbi-'}
        #    cp ${pyroot}/cbi/$MolName.py $Dir$Name.py
        #elif [ `echo $MolName | grep cbl-` ]; then
        #    origMol=$MolName
        #    MolName=${MolName#'cbl-'}
        #    #Name=${Name#'cbl-'}
        #    cp ${pyroot}/cbl/$MolName.py $Dir$Name.py
        #else
        #    for tmp in ${pydirs}; do
        #        [ -e "${tmp}/${MolName}.py" ] && tmpdir=${tmp}
        #    done
        #    cp ${tmpdir}/$MolName.py $Dir$Name.py
        #fi
        
        # pre-modification
        #[ "`echo $Name | grep 'act'`" ] && actmod $Name $Dir
        
        # Modification of python script and omit option
        ResName=
        CountOmit=1
        # opts refers to options of one file
        for opt in ${opts[@]};do
            
            . ~/clones/splited/modopt.sh #.
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
            . ${SplDir}modsh.sh #.
        fi # the end of chain branch
    done # the end of one filename loop
    # chain processing -----------------------------------------------
    if [ ${ischain} = y ]; then
        chain_or_dist=Chain
        nindex=$nchain
        . ${SplDir}modsh_chain.sh #.
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
    echo ''
done < ${RefDir}testinp # %%%-------------------------------------x---------------------%%%

# fullpack processing ----------------------------------------------------------------
if [ ${is_fullpack} = y ]; then
    chain_or_dist=fullpack
    nindex=
    . ${SplDir}modsh_chain.sh #.
fi

# qsub processing --------------------------------------------------------------------
[ $fillnode = y ] && sed -i -e "s/fillnode=n/fillnode=y/g" ${Dir}qsub.sh
sed -i -e "s/usecore=.*/usecore=$usecore/g" ${Dir}qsub.sh
[ ${n_node} -ge 2 ] && [ `expr ${n_node}` ] && sed -i -e "s/n_node=.*/n_node=${n_node}/g" ${Dir}qsub.sh
[ ${isdistribute} = y ] && {
    chain_or_dist=Distribute
    nindex=
    . ${SplDir}modsh_chain.sh #.
}

# print setting -----------------------------------------------------------------------
echo "-------------- option list -----------------"
echo "Omit position = ${OmitOptPos[@]}"
echo "OrzVer = ${OrzVer}"
echo "fillnode option is $fillnode"
echo "the number of core = $usecore"
echo "n_node = $n_node"
echo "fullpack option is $is_fullpack"
echo "--------------------------------------------"
echo "Normal termination                          "
