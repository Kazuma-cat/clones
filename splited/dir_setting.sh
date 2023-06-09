RefDir=~kazuma/clones/
SplDir=~kazuma/clones/splited/
export pyroot=~kazuma/clones/pyFRgeom
export geomroot=~/clones/geom2
chkxroot=~kazuma/clones/chkx2
#tmps=(pyfile_benzalkane3 pyfile_general pyfile_polyene Cbl)
#tmps=(pyfile_benzalkane3 pyfile_general pyfile_polyene TrueCbi)

tmps=(pyfile_benzalkane3 pyfile_general pyfile_polyene)
for tmp in ${tmps[@]}; do
    pydirs="${pydirs[@]} ${pyroot}/${tmp}"
done
echo $chkxroot
if [ $chkxroot = ~kazuma/clones/chkx ]; then
    echo "chkxroot : $chkxroot"
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
fi
