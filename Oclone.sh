#!/bin/bash
export RefDir=~kazuma/clones
export geomroot=~kazuma/clones/geom
export orcaroot=~kazuma/clones/orcapack
export dir=.
tmps=(pf_benzalkane2 pyfile_general cbi)
for tmp in ${tmps[@]}; do
    geomdirs="${geomdirs[@]} ${geomroot}/${tmp}"
done
export geomdirs
. ${orcaroot}/func_Oclone.sh

usecore=16
omp=1
nchain=1
is_chain=n
scf_niter=125

cp ${RefDir}/qsub.sh $dir
chmod +x $dir/qsub.sh
while read -a line; do
    [ -z ${line} ] && continue
    [ "`echo ${line[@]} | grep '!!'`" ] && continue
    [ "`echo ${line[@]} | grep '!'`" ] && {
        [ "`echo $opt | grep 'usecore='`" ] && usecore=${opt:8}
        [ "`echo $opt | grep 'omp='`" ] && omp=${opt:4}
        continue
    }
    names=
    . ${orcaroot}/OReadInp.sh ${line[@]} # OReadInp
    
    [ "`echo ${names[@]} | grep 'Error'`" ] && {
        echo "Error: names variable contains inapproprite string, names='${names[@]}'"
        exit 1
    }
    for name in $names; do
        charge=0
        mult=1
        keyword=
        echo $name
        splited_name=(${name//_/ })
        MolName=${splited_name[0]}
        #for tmp in ${geomdirs}; do
        #    [ -e "${tmp}/${MolName}.py" ] && tmpdir=${tmp}
        #done
        #cp ${orcaroot}/orcabase.inp $dir/$name.inp
        echo $MolName
        func_xyz2orca $name $MolName # xyz to inp
        #sed -i -e "s/chk=/chk=$name.chk/g" $dir/$name.gjf
        sed -i -e "s/_aug_np/$usecore/g" $dir/$name.inp
        for word in ${splited_name[@]}; do
            case $word in
                $MolName)
                    continue;;
                chain)
                    is_chain=y ;;
                b3lyp)
                    keyword="${keyword} b3lyp";;                
                b2plyp)
                    keyword="${keyword} b2plyp";;
                STEOM-DLPNO-CCSD)
                    keyword="${keyword} STEOM-DLPNO-CCSD";;
                std-def2svp)
                    keyword="${keyword} def2-svp def2/j RIJCOSX TightSCF D3BJ";;
                def2svp-RIJ)
                    keyword="${keyword} def2-svp def2-TZVPP/C def2/j RIJCOSX";;
                std-def2tzvpp)
                    keyword="${keyword} def2-tzvpp def2/j RIJCOSX TightSCF D3BJ";;
                std-def2qzvp)
                    keyword="${keyword} def2-qzvp def2/j RIJCOSX TightSCF D3BJ";;
                std-def2qzvpp)
                    keyword="${keyword} def2-qzvpp def2/j RIJCOSX TightSCF D3BJ";;
                std2-sto3g)
                    keyword="${keyword} sto-3g def2/jk RIJCOSX D3BJ";;
                std2-def2tzvpp)
                    keyword="${keyword} def2-tzvpp def2/j RIJCOSX D3BJ";;
                RIMP2-def2svp)
                    keyword="${keyword} RI-MP2 def2-svp def2-svp/C def2/j RIJCOSX";;
                RIMP2-def2tzvp)
                    keyword="${keyword} RI-MP2 def2-tzvp def2-tzvp/C def2/j RIJCOSX";;
                RIMP2-def2tzvpp)
                    keyword="${keyword} RI-MP2 def2-tzvpp def2-tzvpp/C def2/j RIJCOSX";;
                SOSCF-KDIIS)
                    keyword="${keyword} SOSCF KDIIS";;
                *)
                    if [ "`echo $word | grep 'mem'`" ]; then
                        tmp=${word:3}
                        memamount=${tmp: 0:-1}
                        memunit=${tmp: -1}
                        [ $memunit = M ] || [ $memunit = G ] || { echo 'Error: improper memory unit'; exit 1;}
                        sed -i -e "s/mem=.*/mem=${memamount}${memunit}B/g" $dir/$name.inp
                    elif [ "`echo $word | grep 'charge='`" ]; then
                        charge=${word: 7}
                    elif [ "`echo $word | grep 'mult='`" ]; then
                        mult=${word: 5}
                    elif [ "`echo $word | grep 'scf-niter='`" ]; then
                        scf_niter=${word: 10}
                    elif [ "`echo $word | grep 'TD='`" ]; then
                        nroot=${word: 3}
                        sed -i -e "s/%block/%tddft nroots 2 END\n%block/g" $dir/$name.inp
                    elif [ "`echo $word | grep 'mdci='`" ]; then
                        nroot=${word: 5}
                        sed -i -e "s/%block/%mdci\nnroots ${nroot}\ndorootwise true\nEND\n%block/g" $dir/$name.inp
                    fi
            esac
        done # end of word loop
        sed -i -e "s|_keyword|$keyword|g" $dir/$name.inp
        sed -i -e "s/_charge/$charge/g" $dir/$name.inp
        sed -i -e "s/_mult/$mult/g" $dir/$name.inp
        sed -i -e "s/_niter/$scf_niter/g" $dir/$name.inp
        sed -i -e "s/%block//g" $dir/$name.inp
        #sed -i -e 's/ jobtype//g' $dir/$name.gjf 
        if [ ${is_chain} = y ]; then
            :
        else
            cp ${orcaroot}/orcash.sh $dir/$name.sh
            sed -i -e "s/JOBNAME=.*/JOBNAME=${name}/g" $dir/${name}.sh
        fi
    done # end of one file edit
    
    if [ ${is_chain} = y ] ; then
        cp ${orcaroot}/orcash_chain.sh $dir/Chain${nchain}.sh
        echo $names
        echo ${names:0:}
        [ ${names:0:1} =  ] && names=${names# }
        sed -i -e "s/JOBNAMES=/JOBNAMES=${names}/g" $dir/Chain${nchain}.sh
        sed -i -e "s/filelist=(/filelist=(Chain${nchain} /g" $dir/qsub.sh
        sed -i -e "s/usecore=.*/usecore=${usecore}/g" $dir/qsub.sh
        sed -i -e "s/omp=.*/omp=${omp}/g" $dir/qsub.sh
        nchain=`expr $nchain + 1`
        is_chain=n
    else
        sed -i -e "s/filelist=(/filelist=(${names} /g" $dir/qsub.sh
        sed -i -e "s/usecore=.*/usecore=${usecore}/g" $dir/qsub.sh
        sed -i -e "s/omp=.*/omp=${omp}/g" $dir/qsub.sh
    fi
done < $orcaroot/OCinp # end of all line loop
