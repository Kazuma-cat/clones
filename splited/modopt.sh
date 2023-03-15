charge=None
case $opt in
    $MolName)
        CountOmit=`expr "$CountOmit" + 1`
        continue;;
    $origMol)
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
        sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PMNR\"/g' $Dir$Name.py
        sed -i -e 's/hint.ImplTypePM =.*/hint.ImplTypePM = "sparse"/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_Active =.*/lct.TCutDOI_Active = 7e-3/g' $Dir$Name.py;;
    newPMNR)
        sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PMNR\"/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py
        sed -i -e 's/hint.ImplTypePM =.*/hint.ImplTypePM = "sparse"/g' $Dir$Name.py
        sed -i -e 's/#lct.PMMaxIt/lct.PMMaxIt/g' $Dir$Name.py
        sed -i -e 's/#lct.PMStep/lct.PMStep/g' $Dir$Name.py
        sed -i -e 's/#hint.PM_AB_thresh/hint.PM_AB_thresh/g' $Dir$Name.py
        sed -i -e 's/#hint.PM_ang_thresh/hint.PM_ang_thresh/g' $Dir$Name.py
        sed -i -e 's/#hint.PM_trunc_thresh/hint.PM_trunc_thresh/g' $Dir$Name.py
        ;;
    noniterPM)
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = False/g' $Dir$Name.py
        sed -i -e 's/hint.ImplTypePM =.*/hint.ImplTypePM = "incore"/g' $Dir$Name.py
        ;;
    nontruncincorePM)
        sed -i -e 's/hint.PM_nontrunc_incore =.*/hint.PM_nontrunc_incore = True/g' $Dir$Name.py
        ;;
    PMNR-nJ)
        sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PMNR-nJ\"/g' $Dir$Name.py ;;
    PSM1)
        sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
        sed -i -e 's/lct.LocPower =.*/lct.LocPower = 1/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_Active =.*/lct.TCutDOI_Active = 7e-3/g' $Dir$Name.py;;
    PSM2)
        sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
        sed -i -e 's/lct.LocPower =.*/lct.LocPower = 2/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py;;
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
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py
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
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py
        MSorz=y;;
    MS5orz)
        sed -i -e 's/lct.test.*/#lct.test = False/g' $Dir$Name.py
        sed -i -e 's/lct.DoPNO.*/#lct.DoPNO = True/g' $Dir$Name.py
        sed -i -e 's/lct.UseOrthPNOs.*/#lct.UseOrthPNOs = True/g' $Dir$Name.py
        sed -i -e 's/lct.RIMP2.*/#lct.RIMP2 = False/g' $Dir$Name.py
        sed -i -e 's/hint.trafo_algo.*/#hint.trafo_algo = "RI-SemiDirect-Disk"/g' $Dir$Name.py
        MS5orz=y;;
    orzgit2)
        orzgit2=y
        ;;
    orzmod)
        sed -i -e 's/#hint.PM_nontrunc_incore =.*/hint.PM_nontrunc_incore = False/g' $Dir$Name.py
        orzmod=y
        ;;
    stdCrude)
        sed -i -e 's/lct.DoTwoStepGuess =.*/lct.DoTwoStepGuess = True/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI =.*/lct.TCutDOI = 5e-4/g' $Dir$Name.py
        sed -i -e 's/lct.TCutPairs_Crude =.*/lct.TCutPairs_Crude = 1e-5/g' $Dir$Name.py;;
    stdCrude2)
        sed -i -e 's/lct.DoTwoStepGuess =.*/lct.DoTwoStepGuess = True/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI =.*/lct.TCutDOI = 3.33e-4/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_Crude =.*/lct.TCutDOI_Crude = 3.33e-3/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_Active =.*/lct.TCutDOI_Active = 7e-3/g' $Dir$Name.py
        sed -i -e 's/lct.TCutPairs_Crude =.*/lct.TCutPairs_Crude = 6.66e-7/g' $Dir$Name.py;;
    newstdCrude)
        sed -i -e 's/lct.DoTwoStepGuess =.*/lct.DoTwoStepGuess = True/g' $Dir$Name.py
        sed -i -e 's/lct.TCutPairs\s*=.*/lct.TCutPairs = 3.33e-6/g' $Dir$Name.py
        #sed -i -e 's/lct.TCutDOI_Active =.*/lct.TCutDOI_Active = 7e-3/g' $Dir$Name.py 
        sed -i -e 's/lct.TCutDOI =.*/lct.TCutDOI = 3.33e-4/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_PAO =.*/lct.TCutDOI_PAO = 1e-2/g' $Dir$Name.py
        sed -i -e 's/lct.TCutPairs_Crude =.*/lct.TCutPairs_Crude = 6.66e-7/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_Crude =.*/lct.TCutDOI_Crude = 3.33e-3/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_PAO_Crude =.*/lct.TCutDOI_PAO_Crude = 1e-2/g' $Dir$Name.py
        ;;
    stdnocrude)
        sed -i -e 's/lct.DoTwoStepGuess =.*/lct.DoTwoStepGuess = False/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI =.*/lct.TCutDOI = 1e-3/g' $Dir$Name.py
        sed -i -e 's/lct.TCutPairs\s*=.*/lct.TCutPairs = 3.33e-6/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_PAO =.*/lct.TCutDOI_PAO = 1e-2/g' $Dir$Name.py;;
    nocrude)
        sed -i -e 's/lct.DoTwoStepGuess =.*/lct.DoTwoStepGuess = False/g' $Dir$Name.py;;
    newnocrude)
        sed -i -e 's/lct.DoTwoStepGuess =.*/lct.DoTwoStepGuess = False/g' $Dir$Name.py
        sed -i -e 's/lct.TCutPairs\s*=.*/lct.TCutPairs = 3.33e-6/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI =.*/lct.TCutDOI = 3.33e-4/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_PAO =.*/lct.TCutDOI_PAO = 1e-2/g' $Dir$Name.py;;
    PrintAllEps)
        sed -i -e 's/lct.PrintAllEps =.*/lct.PrintAllEps = True/g' $Dir$Name.py;;
    oldPAO)
        sed -i -e 's/lct.UsePAOs =.*/lct.UsePAOs = True/g' $Dir$Name.py
        sed -i -e 's/lct.FormLVOs =.*/lct.FormLVOs = False/g' $Dir$Name.py
        sed -i -e 's/lct.UseNewDomain =.*/lct.UseNewDomain = False/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py;;
    newPAO)
        sed -i -e 's/lct.UsePAOs =.*/lct.UsePAOs = True/g' $Dir$Name.py
        sed -i -e 's/lct.FormLVOs =.*/lct.FormLVOs = False/g' $Dir$Name.py
        sed -i -e 's/lct.UseNewDomain =.*/lct.UseNewDomain = True/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py;;
    FBPAO)
        sed -i -e 's/lct.UsePAOs =.*/lct.UsePAOs = True/g' $Dir$Name.py
        sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PSM\"/g' $Dir$Name.py
        sed -i -e 's/lct.LocPower =.*/lct.LocPower = 1/g' $Dir$Name.py
        sed -i -e 's/lct.FormLVOs =.*/lct.FormLVOs = False/g' $Dir$Name.py
        sed -i -e 's/lct.UseNewDomain =.*/lct.UseNewDomain = True/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = True/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_Active =.*/lct.TCutDOI_Active = 1e-2/g' $Dir$Name.py;;
    PMPAO)
        sed -i -e 's/lct.UsePAOs =.*/lct.UsePAOs = True/g' $Dir$Name.py
        sed -i -e 's/lct.LocMet =.*/lct.LocMet = \"PMNR\"/g' $Dir$Name.py
        sed -i -e 's/hint.ImplTypePM =.*/hint.ImplTypePM = "incore"/g' $Dir$Name.py
        sed -i -e 's/lct.FormLVOs =.*/lct.FormLVOs = False/g' $Dir$Name.py
        sed -i -e 's/lct.UseNewDomain =.*/lct.UseNewDomain = True/g' $Dir$Name.py
        sed -i -e 's/lct.LocRecursive =.*/lct.LocRecursive = False/g' $Dir$Name.py
        sed -i -e 's/lct.TCutDOI_Active =.*/lct.TCutDOI_Active = 1e-2/g' $Dir$Name.py;;
    DOIActPAO)
        sed -i -e 's/lct.TCutDOI_Active =.*/lct.TCutDOI_Active = 1.75e-2/g' $Dir$Name.py;;
    NaivePAO)
        sed -i -e 's/lct.UseNaiveMapPAOs\s*=.*/lct.UseNaiveMapPAOs = True/g' $Dir$Name.py;;
    casscf)
        sed -i -e 's/hint.trafo_algo.*/hint.trafo_algo = "RI-Incore-RMA"/g' $Dir$Name.py
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
    RIMP2)
        sed -i -e 's/lct.Ansatz =.*/lct.Ansatz = "RIMP2"/g' $Dir$Name.py ;;
    PNO-NEVPT2)
        sed -i -e 's/icmr.method =.*/icmr.method = "nevpt2"/g' $Dir$Name.py
        sed -i -e 's/lct.Ansatz =.*/lct.Ansatz = "PNO-NEVPT2"/g' $Dir$Name.py ;;
    PNO-CASPT2)
        sed -i -e 's/icmr.method =.*/icmr.method = "caspt2"/g' $Dir$Name.py
        sed -i -e 's/lct.Ansatz =.*/lct.Ansatz = "PNO-CASPT2"/g' $Dir$Name.py ;;
    NEVPT2)
        sed -i -e 's/icmr.method =.*/icmr.method = "nevpt2"/g' $Dir$Name.py
        sed -i -e 's/lct.Ansatz =.*/lct.Ansatz = "NEVPT2"/g' $Dir$Name.py ;;
    CASPT2)
        sed -i -e 's/icmr.method =.*/icmr.method = "caspt2"/g' $Dir$Name.py
        sed -i -e 's/lct.Ansatz =.*/lct.Ansatz = "CASPT2"/g' $Dir$Name.py ;;
    calctest)
        cp ${RefDir}calctest $Dir;;
    DOIFabs)
        sed -i -e 's/lct.DoDOIFabs =.*/lct.DoDOIFabs = True/g' $Dir$Name.py ;;
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
    moread-sto6g)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_sto6g[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-sto6g-svp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_sto6g_svp[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-sto6g-tzvpp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_sto6g_tzvpp[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-def2svp-reorder)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_def2svp_reorder[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread2-def2svp-reorder)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx2_def2svp_reorder[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-def2tzvp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_def2tzvp[@]}; do
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
    moread2-loc-def2svp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx2_loc_def2svp[@]}; do
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
    moread-sto3g-lowspin)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_sto3g_lowspin[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-b3lyp-lowspin)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_b3lyp_lowspin[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-b3lyp-sto3g-def2svp-lowspin)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_b3lyp_sto3g_def2svp_lowspin[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread2-b3lyp-sto3g-def2svp-lowspin)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx2_b3lyp_sto3g_def2svp_lowspin[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-reorder-b3lyp-sto3g-def2svp-lowspin)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_reorder_b3lyp_sto3g_def2svp_lowspin[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-cas-cbl-sto3g-def2svp-PNOCAS)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_cas_cbl_sto3g_def2svp_PNOCAS[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-locDV-cbl)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx2_locDV_low_cbl_b3lyp_sto3g_def2svp[@]}; do
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
    moread2-cbl-mycas2)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx2_cbl_mycas2[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread2-cbl-mycasloc1)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx2_cbl_mycasloc1[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-testcas)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_testcas[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-MScas-cbls-sto6g-tzvpp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_MScas_cbls_sto6g_tzvpp[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-MScas2-cbls-sto6g-tzvpp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_MScas2_cbls_sto6g_tzvpp[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-MScas3-cbls-svp-tzvpp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_MScas3_cbls_svp_tzvpp[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-casscf-sto6g-svp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_casscf_sto6g_svp[@]}; do
            [ -e "${tmp}/${MolName}.chkx" ] && {
                cp ${tmp}/${MolName}.chkx $Dir$Name.chkx
                tmpchk=y
            }
        done
        [ ${tmpchk} = n ] && { echo "Error: ${MolName}.chkx could not be found."; exit 1; } ;;
    moread-casscf-sto6g-tzvpp)
        sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
        tmpchk=n
        for tmp in ${chkx_casscf_sto6g_tzvpp[@]}; do
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
    distribute)
        isdistribute=y ;;
    nolct)
        is_nolct=y ;;
    locCA)
        loctype=CA ;;
    locDV)
        loctype=DV ;;
    locnC)
        loctype=nC ;;
    Mbasis=sto3g)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("sto-3g") # Molecule Basis Set/g' $Dir$Name.py ;;
    Mbasis=sto6g)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("sto-6g") # Molecule Basis Set/g' $Dir$Name.py ;;
    Mbasis=sto6g)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("sto-6g") # Molecule Basis Set/g' $Dir$Name.py ;;
    Mbasis=def2svp)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("def2-SVP") # Molecule Basis Set/g' $Dir$Name.py ;;
    Mbasis=def2tzvp)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("def2-TZVP") # Molecule Basis Set/g' $Dir$Name.py ;; 
    Mbasis=def2tzvpp)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("def2-TZVPP") # Molecule Basis Set/g' $Dir$Name.py ;;
    Mbasis=ccpvdz)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("cc-pvdz") # Molecule Basis Set/g' $Dir$Name.py ;;
    Mbasis=svptzvpp)
        sed -i -e 's/.*Molecule Basis Set/qatom.basis = baslib("def2-SVP") # Molecule Basis Set/g' $Dir$Name.py
        mybasis $Dir$Name.py svptzvpp $origmolname;;
    b3lyp)
        sed -i -e 's|# add option|scf.dft_ang = 11\nscf.dft_intacc = 13. / 3.\nscf.tol_density = 1e-3\nscf.dft_xc = ["hyb_gga_xc_b3lyp"]\n# add option|g' $Dir$Name.py
        ;;
    *)
        if [ "`echo $opt | grep 'Tj'`" ];then
            tmpj=${opt:2}
            sed -i -e "s/hint.jacobi_thresh.*/hint.jacobi_thresh = ${tmpj}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'Tl'`" ];then
            tmpl=${opt:2}
            sed -i -e "s/hint.loc_thresh.*/hint.loc_thresh = ${tmpl}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'locthresh'`" ];then
            tmpl=${opt:10}
            sed -i -e "s/hint.loc_thresh.*/hint.loc_thresh = ${tmpl}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'Tr'`" ];then
            tmpr=${opt:2}
            sed -i -e "s/hint.kscal.*/hint.kscal = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutPNOrho0'`" ];then
            tmpr=${opt:12}
            sed -i -e "s/lct.TCutPNOrho0.*/lct.TCutPNOrho0 = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutPairs='`" ];then
            tmpr=${opt:10}
            #sed -i -e "s/lct.TCutPairs[^\S][^\S][^\S][^\S][^\S][^\S][^\S]=.*/lct.TCutPairs = ${tmpr}/g" $Dir$Name.py
            sed -i -e "s/lct.TCutPairs\s*=.*/lct.TCutPairs = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutPre'`" ];then
            tmpr=${opt:8}
            sed -i -e "s/lct.TCutPre.*/lct.TCutPre = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutPairsCrude='`" ];then
            tmpr=${opt:15}
            echo $tmpr
            sed -i -e "s/lct.TCutPairs_Crude =.*/lct.TCutPairs_Crude = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutDOI='`" ];then
            tmpr=${opt:8}
            sed -i -e "s/lct.TCutDOI [^\S]*=.*/lct.TCutDOI = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutDOIPAO='`" ];then
            tmpr=${opt:11}
            sed -i -e "s/lct.TCutDOI_PAO\s*=.*/lct.TCutDOI_PAO = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutDOICrude='`" ];then
            tmpr=${opt:13}
            sed -i -e "s/lct.TCutDOI_Crude\s*=.*/lct.TCutDOI_Crude = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutDOIPAOCrude='`" ];then
            tmpr=${opt:16}
            sed -i -e "s/lct.TCutDOI_PAO_Crude\s*=.*/lct.TCutDOI_PAO_Crude = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'TCutDOIActive='`" ];then
            tmpr=${opt:14}
            sed -i -e "s/lct.TCutDOI_Active.*/lct.TCutDOI_Active = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'PMMaxIt'`" ];then
            tmpr=${opt:8}
            sed -i -e "s/lct.PMMaxIt =.*/lct.PMMaxIt = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'PMStep'`" ];then
            tmpr=${opt:6}
            sed -i -e "s/lct.PMStep =.*/lct.PMStep = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'PMAB='`" ];then
            tmpr=${opt:5}
            sed -i -e "s/hint.PM_AB_thresh =.*/hint.PM_AB_thresh = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'PMang='`" ];then
            tmpr=${opt:6}
            sed -i -e "s/hint.PM_ang_thresh =.*/hint.PM_ang_thresh = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'PMtrunc='`" ];then
            tmpr=${opt:8}
            sed -i -e "s/hint.PM_trunc_thresh =.*/hint.PM_trunc_thresh = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'lvlshift'`" ];then
            tmpr=${opt:9}
            sed -i -e "s/icmr.pt.lvl_shift =.*/icmr.pt.lvl_shift = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'ipeashift'`" ];then
            tmpr=${opt:10}
            sed -i -e "s/icmr.pt.ipeashift =.*/icmr.pt.ipeashift = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'charge='`" ];then
            tmp=${opt:7}
            sed -i -e "s/charge=0/charge=${tmp}/g" $Dir$Name.py
            charge=${tmp}
            origfrozen=`grep '# orig frozen ... ' $Dir$Name.py`
            origfrozen=${origfrozen#'# orig frozen ... '}
            origclosed=`grep '# orig closed ... ' $Dir$Name.py` 
            origclosed=${origclosed#'# orig closed ... '}
            closed="`echo "scale=2; $origclosed - ($charge)/2 " | bc`"
            echo "closed = $closed"
            [ ${closed: -1} -ne 0 ] && exit "uncorrect electron number was detected"
            sed -i -e "s/# orb info end ------------/# closed including charge ... ${closed}\n# orb info end ------------/g" $Dir$Name.py
            closed=`printf '%.0f\n' $closed`
            #casclosed=$(($closed + $origfrozen))
            casclosed=`python3 -c "print(int($closed + $origfrozen))"`
            echo "casclosed = $casclosed"
            sed -i -e "s/casscf.closed = .*/casscf.closed = \[$casclosed\]/g" $Dir$Name.py
            sed -i -e "s/icmr.closed = .*/icmr.closed = \[$closed\]/g" $Dir$Name.py
            
        elif [ "`echo $opt | grep 'mult='`" ];then
            tmp=${opt:5}
            sed -i -e "s/mult=1/mult=${tmp}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'maxloop'`" ];then
            tmp=${opt:7}
            sed -i -e "s/scf.maxloop.*/scf.maxloop = ${tmp}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'lctmaxiter'`" ];then
            tmpr=${opt:10}
            sed -i -e "s/lct.MaxIter =.*/lct.MaxIter = ${tmpr}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'act='`" ];then
            tmp=${opt:4}
            actocc=${tmp%%-*}
            actvir=${tmp##*-}
            # casscf nactive modification
            tmp2=`awk '/casscf.closed.*/ {print $0}' $Dir$Name.py`;tmp3=`awk '/casscf.occ.*/ {print $0}' $Dir$Name.py`;
            tmp2=${tmp2##*\[}; tmp2=${tmp2%%\]*}; tmp3=${tmp3##*\[}; tmp3=${tmp3%%\]*}; tmp2=`echo $tmp2`; tmp3=`echo $tmp3`
            nclosed=$tmp2
            nocc=$tmp3
            w_closed=`expr ${nclosed} + ${nocc} - ${actocc}`
            w_occ=`expr ${actocc} + ${actvir}`
            echo "w_closed,w_occ = (${w_closed},${w_occ}) in casscf region"
            sed -i -e "s/casscf.closed.*/casscf.closed = [${w_closed}]/g" $Dir$Name.py
            sed -i -e "s/casscf.occ.*/casscf.occ = [${w_occ}]/g" $Dir$Name.py
            # icmr nactive modification
            tmp4=`awk '/icmr.closed.*/ {print $0}' $Dir$Name.py`;tmp5=`awk '/icmr.occ.*/ {print $0}' $Dir$Name.py`;
            tmp4=${tmp4##*\[}; tmp4=${tmp4%%\]*}; tmp5=${tmp5##*\[}; tmp5=${tmp5%%\]*}; tmp4=`echo $tmp4`; tmp5=`echo $tmp5`
            nclosed=$tmp4
            nocc=$tmp5
            w_closed=`expr ${nclosed} + ${nocc} - ${actocc}`
            w_occ=`expr ${actocc} + ${actvir}`
            echo "w_closed,w_occ = (${w_closed},${w_occ}) in icmr region"
            sed -i -e "s/icmr.closed.*/# info ...\n#log nclosed=${nclosed}\n#log nocc=${nocc}\nicmr.closed = [${w_closed}]/g" $Dir$Name.py
            sed -i -e "s/icmr.occ.*/icmr.occ = [${w_occ}]/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'roots='`" ];then
            tmp=${opt:6}
            sed -i -e "s/casscf.roots.*/casscf.roots = \{${tmp}\}/g" $Dir$Name.py
            sed -i -e "s/icmr.roots.*/icmr.roots = \{${tmp}\}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'StackSize='`" ];then
            echo "opt = ($opt)"
            tmp=${opt:10}
            sed -i -e "s/lct.StackSize =.*/lct.StackSize = ${tmp}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'DOIPower='`" ];then
            #echo "opt = ($opt)"
            tmp=${opt:9}
            sed -i -e "s/lct.DOIPower =.*/lct.DOIPower = ${tmp}/g" $Dir$Name.py
        elif [ "`echo $opt | grep 'moread-'`" ];then
            sed -i -e 's/#scf.guess = "moread"/scf.guess = "moread"/g' $Dir$Name.py
            tmp=${opt//'moread-'/''}
            tmp=${tmp//'-'/'/'}
            if [ -e "${chkxroot}/${tmp}/${MolName}.chkx" ]; then
                cp ${chkxroot}/${tmp}/${MolName}.chkx $Dir$Name.chkx
            else
                echo "Error: ${MolName}.chkx could not be found."
                exit 1
            fi
        elif [ "`echo $opt | grep 'nrandomize'`" ];then
            sed -i -e "s/hint.randomize.*/hint.randomize = True/g" $Dir$Name.py
        else
            echo "Pyfile Modification Error: ${opt} option is not defined"
        fi
esac # end of opt modification

