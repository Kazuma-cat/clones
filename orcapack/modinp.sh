#b3lyp)
#keyword="${keyword} b3lyp";;
#M06)
#    keyword="${keyword} m06";;
#tpssh)
#    keyword="${keyword} tpssh";;
#b2plyp)
#    keyword="${keyword} b2plyp";;
#STEOM-DLPNO-CCSD)
#keyword="${keyword} STEOM-DLPNO-CCSD";;
simples="b3lyp m06 tpssh b2plyp STEOM-DLPNO-CCSD D3BJ D3zero def2-svp def2-tzvp def2/j rijcosx opt freq tightscf"
for word in ${splited_name[@]}; do
    case $word in
        $MolName)
            continue;;
        chain)
            is_chain=y ;;
        std-def2svp)
            keyword="${keyword} def2-svp def2/j RIJCOSX TightSCF D3BJ";;
        def2svp-RIJ)
            keyword="${keyword} def2-svp def2-TZVPP/C def2/j RIJCOSX";;
        std-def2tzvp)
            keyword="${keyword} def2-tzvp def2/j RIJCOSX TightSCF D3BJ";;
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
        rijcosx)
            keyword="${keyword} def2/j RIJCOSX";;
        def2-tzvp-rijcosx)
            keyword="${keyword} def2-tzvp def2-tzvp/C def2/j RIJCOSX";;
        *)
            for tmp in $simples; do
                [ $tmp = $word ] && keyword="${keyword} ${word}"
            done
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
            elif [ "`echo $word | grep 'td=[0-9]\+-[0-9]\+'`" ]; then
                tmp=${word: 3}
                tmp=(${tmp//'-'/' '})
                nroot=${tmp[0]}
                maxdim=${tmp[1]}
                sed -i -e "s/%block/%tddft\nnroots $nroot\nmaxdim $maxdim\nEND\n%block/g" $dir/$name.inp
            elif [ "`echo $word | grep 'mdci='`" ]; then
                nroot=${word: 5}
                sed -i -e "s/%block/%mdci\nnroots ${nroot}\ndorootwise true\nEND\n%block/g" $dir/$name.inp
            fi
    esac
done
sed -i -e "s/_aug_np/$usecore/g" $dir/$name.inp
sed -i -e "s|_keyword|$keyword|g" $dir/$name.inp
sed -i -e "s/_charge/$charge/g" $dir/$name.inp
sed -i -e "s/_mult/$mult/g" $dir/$name.inp
sed -i -e "s/_niter/$scf_niter/g" $dir/$name.inp
sed -i -e "s/%block//g" $dir/$name.inp
        
