#!/bin/bash
export RefDir=~kazuma/clones
export geomroot=~kazuma/clones/geom
export gaussroot=~kazuma/clones/Gpart
export dir=.
tmps=(pf_benzalkane2 pyfile_general Cbl)
for tmp in ${tmps[@]}; do
    geomdirs="${geomdirs[@]} ${geomroot}/${tmp}"
done
export geomdirs
. ${gaussroot}/func_Gclone.sh


nchain=1
is_chain=n

cp ${RefDir}/qsub.sh $dir
chmod +x $dir/qsub.sh
while read -a line; do
    [ -z ${line} ] && continue
    [ "`echo ${line[@]} | grep '!!'`" ] && continue
    [ "`echo ${line[@]} | grep '!'`" ] && continue
    names=
    . ${gaussroot}/GReadInp.sh ${line[@]} # GReadInp
    #names=`bash ${gaussroot}/GReadInp.sh ${line[@]}`
    #echo ${names[@]}
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'"
        exit 1
    }
    for name in $names; do
        charge=0
        spin=1
        
        echo $name
        splited_name=(${name//_/ })
        MolName=${splited_name[0]}
        for tmp in ${geomdirs}; do
            [ -e "${tmp}/${MolName}.py" ] && tmpdir=${tmp}
        done
        cp ${gaussroot}/GaussBase.gjf $dir/$name.gjf
        func_xyz2gjf $name $MolName # xyz to gjf
        sed -i -e "s/chk=/chk=$name.chk/g" $dir/$name.gjf
        for word in ${splited_name[@]}; do
            case $word in
                $MolName)
                    continue;;
                opt)
                    sed -i -e 's/jobtype/opt jobtype/g' $dir/$name.gjf ;;
                GD3BJ)
                    sed -i -e 's/jobtype/EmpiricalDispersion=GD3BJ jobtype/g' $dir/$name.gjf ;;
                b3lyp)
                    sed -i -e 's/method/b3lyp/g' $dir/$name.gjf ;;
                def2svp)
                    sed -i -e 's/base/def2svp/g' $dir/$name.gjf ;;
                TD2)
                    sed -i -e 's/jobtype/TD=(nstate=2)jobtype/g' $dir/$name.gjf ;;
                chain)
                    is_chain=y ;;
                *)
                    if [ "`echo $word | grep 'mem'`" ]; then
                        tmp=${word:3}
                        memamount=${tmp: 0:-1}
                        memunit=${tmp: -1}
                        [ $memunit = M ] || [ $memunit = G ] || { echo 'Error: improper memory unit'; exit 1;}
                        sed -i -e "s/mem=.*/mem=${memamount}${memunit}B/g" $dir/$name.gjf
                    fi
            esac
        done # end of word loop
        sed -i -e "s/charge/$charge/g" $dir/$name.gjf
        sed -i -e "s/spin/$spin/g" $dir/$name.gjf 
        sed -i -e 's/ jobtype//g' $dir/$name.gjf 
        if [ ${is_chain} = y ]; then
            :
        else
            cp ${gaussroot}/GaussBase.sh $dir/$name.sh
            sed -i -e "s/JOBNAME=.*/JOBNAME=${name}/g" $dir/${name}.sh
        fi
    done # end of one file edit
    
    if [ ${is_chain} = y ] ; then
        cp ${gaussroot}/GaussBase_chain.sh $dir/Chain${nchain}.sh
        echo $names
        echo ${names:0:}
        [ ${names:0:1} =  ] && names=${names# }
        sed -i -e "s/JOBNAMES=/JOBNAMES=${names}/g" $dir/Chain${nchain}.sh
        sed -i -e "s/filelist=(/filelist=(Chain${nchain} /g" $dir/qsub.sh
        nchain=`expr $nchain + 1`
        is_chain=n
    else
        sed -i -e "s/filelist=(/filelist=(${names} /g" $dir/qsub.sh
    fi
done < $gaussroot/GCinp # end of all line loop
