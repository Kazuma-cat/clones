#!/bin/bash
# check whether molecule original python script in clone directory
count=0
# simple option
opt_method="PMPAO FBPAO newPAO oldPAO Ref RIMP2 CASPT2 PNO-CASPT2 NEVPT2 PNO-NEVPT2 calctest casscf b3lyp"
opt_moread="moreadonly moread-sto3g moread-sto3g-lowspin moread-b3lyp-lowspin moread-b3lyp-sto3g-def2svp-lowspin moread2-b3lyp-sto3g-def2svp-lowspin moread-reorder-b3lyp-sto3g-def2svp-lowspin moread-def2svp moread-def2svp-reorder moread2-def2svp-reorder moread-loc-def2svp moread2-loc-def2svp moread-def2tzvp moread-locDV-cbl moread-cas-cbl-sto3g-def2svp-PNOCAS moread-casscf moread2-cbl-mycas2 moread2-cbl-mycasloc1 moread-testcas moread-MScas-cbls-sto6g-tzvpp moread-MScas2-cbls-sto6g-tzvpp maxloop0 moread-MScas3-cbls-svp-tzvpp moread-sto6g moread-sto6g-svp moread-sto6g-tzvpp moread-casscf-sto6g-svp moread-casscf-sto6g-tzvpp"
opt_other="orzgit2 orzmod chain distribute nolct MS5orz noGA3 CMO locCA locDV locnC DOIFabs stdCrude stdCrude2 newstdCrude stdnocrude nocrude newnocrude noniterPM nontruncincorePM NaivePAO"
defined_opts="${opt_method} ${opt_moread} ${opt_other}"

# number option
opts_num="Tl locthresh Tj Tr TCutPNOrho0 TCutPairs TCutPre PMMaxIt PMStep PMAB PMang PMtrunc lvlshift ipeashift lctmaxiter Mbasis charge mult act roots StackSize DOIPower maxloop TCutDOI TCutDOIPAO TCutDOICrude TCutDOIPAOCrude TCutDOIActive  TCutPairsCrude"

detect_opt=n
for opt in $@; do
    # molecular name detector --------------------------------------------------------------------
    [ "$count" -eq 0 ] && {
        MolName="$opt"
        if [ ${MolName:0:7} = 'polyene' ]; then
            IFSBACK=$IFS
            IFS=_
            tmps=(${MolName})
            IFS=$IFSBACK
            Cmin=${tmps[1]:-0}
            Cmax=${tmps[2]:-300}
            for tmp in ${pydirs[@]}; do
                filenames=(${filenames[@]} `ls ${tmp}/c*.py`)
            done
            #filenames=(`ls ${PyDir1}c*.py` `ls ${PyDir2}c*.py`)
            names=
            for filename in ${filenames[@]}; do
                filename=`basename ${filename}`
                Cn=`echo $filename | grep -o 'c[0-9]\+'`
                Hn=`echo $filename | grep -o 'h[0-9]\+'`
                Cn=${Cn:1}
                Hn=${Hn:1}
                HnM2=`expr ${Hn} - 2`
                [ ${Cn} -eq ${HnM2} ] && [ ${Cn} -ge ${Cmin} ] && [ ${Cn} -le ${Cmax} ] && {
                    names="${names} ${filename%.py}"
                    #echo ${names}
                }
                
            done
        elif [ ${MolName:0:12} = 'benz-polyene' ]; then
            IFSBACK=$IFS
            IFS=_
            tmps=(${MolName})
            IFS=$IFSBACK
            Cmin=${tmps[1]:-0}
            Cmax=${tmps[2]:-300}
            filenames=(`ls ${PyDir1}benz-c*.py` `ls ${PyDir2}benz-c*.py`)
            names=
            for filename in ${filenames[@]}; do
                filename=`basename ${filename}`
                Cn=`echo $filename | grep -o 'c[0-9]\+'`
                Hn=`echo $filename | grep -o 'h[0-9]\+'`
                Cn=${Cn:1}
                Hn=${Hn:1}
                HnM2=`expr ${Hn} - 2`
                [ ${Cn} -eq ${HnM2} ] && [ ${Cn} -ge ${Cmin} ] && [ ${Cn} -le ${Cmax} ] && {
                    names="${names} ${filename%.py}"
                    #echo ${names}
                }
                
            done
        elif [ ${MolName:0:11} = 'benz-alkane' ]; then
            IFSBACK=$IFS
            IFS=_
            tmps=(${MolName})
            IFS=$IFSBACK
            Cmin=${tmps[1]:-0}
            Cmax=${tmps[2]:-300}
            for tmp in ${pydirs}; do
                filenames=(${filenames[@]} `ls ${tmp}/benz-c*.py`)
            done
            names=
            for filename in ${filenames[@]}; do
                filename=`basename ${filename}`
                Cn=`echo $filename | grep -o 'c[0-9]\+'`
                Hn=`echo $filename | grep -o 'h[0-9]\+'`
                Cn=${Cn:1}
                Hn=${Hn:1}
                Cn2P2=`expr ${Cn} \* 2 + 2`
                [ ${Hn} -eq ${Cn2P2} ] && [ ${Cn} -ge ${Cmin} ] && [ ${Cn} -le ${Cmax} ] && {
                    names="${names} ${filename%.py}"
                }
                
            done
            
        else
            names="$MolName"
            if [ `echo $names | grep cbi-` ]; then
                tmp=${MolName#'cbi-'}
                [ -e "${pyroot}/cbi/${tmp}.py" ] || { echo "Name Error: ${MolName}.py could not be found."; exit 1; }
            elif [ `echo $names | grep cbl-` ]; then
                tmp=${MolName#'cbl-'}
                [ -e "${pyroot}/cbl/${tmp}.py" ] || { echo "Name Error: ${MolName}.py could not be found."; exit 1; }
            else
                tmpchk=n
                for tmp in ${pydirs}; do
                    [ -e "${tmp}/${MolName}.py" ] && tmpchk=y
                done
                [ $tmpchk = n ] && { echo "Name Error: ${MolName}.py could not be found."; exit 1; }
            fi
        fi
        
        count=`expr "$count" + 1`
        continue;
    }
    # normal option detector ---------------------------------------------------------------------------
    detect_opt=n
    for defined_opt in ${defined_opts}; do
        [ $opt = chain ] && [ $is_fullpack = y ] && { detect_opt=y; break; }
        [ $opt = $defined_opt ] && {
            tmps="${names}"
            names=
            for tmp in ${tmps}; do
                tmp2=${tmp}_${defined_opt}
                names="${names} $tmp2"
            done
            detect_opt=y
        }
    done
    [ $detect_opt = y ] && continue
    # number's option detector ----------------------------------------------------------------------------------
    detect_optnum=n
    for opt_num in ${opts_num}; do
        [ $opt = chain ] && [ $is_fullpack = y ] && { detect_opt=y; break; }
        [ `echo $opt | grep "${opt_num}="` ] && {
            tmps=${names}
            names=
            tmpset=(${opt//'='/' '})
            optspr=${tmpset[0]}
            optnums=${tmpset[1]//','/' ' }
            for optnum in ${optnums}; do
                for tmp in ${tmps}; do
                    tmp2=${tmp}_${optspr}=${optnum}
                    names="${names} $tmp2"
                done
            done
            detect_optnum=y
        }
    done
    [ $detect_optnum = y ] && continue
    # other option detector ----------------------------------------------------------------------------------
    [ "`echo $opt | grep 'ImplTypePM'`" ] && {
        case $opt in
            ImplTypePM)
                tmps="${names}"
                names=
                for tmp in ${tmps}; do
                    tmp1=${tmp}_incore
                    tmp2=${tmp}_MS
                    names="${names} $tmp1 $tmp2"
                done ;;
            ImplTypePM=incore)
                tmps="${names}"
                names=
                for tmp in "${tmps}"; do
                    tmp1=${tmp}_incore
                    names="${names} ${tmp1}"
                done ;;
            ImplTypePM=MS)
                tmps="${names}"
                names=
                for tmp in "${tmps}"; do
                    tmp1=${tmp}_MS
                    names="${names} $tmp1"
                done ;;
        esac
    }
    [ "`echo $opt | grep 'OnTheFly'`" ] && {
        case $opt in
            OnTheFly)
                tmps="${names}"
                names=
                for tmp in ${tmps}; do
                    tmp1=${tmp}_NotOn
                    tmp2=${tmp}_On
                    names="${names} $tmp1 $tmp2"
                done ;;
            OnTheFly=On)
                tmps="${names}"
                names=
                for tmp in ${tmps}; do
                    tmp2=${tmp}_On
                    names="${names} $tmp2"
                done ;;
            OnTheFly=Not)
                tmps="${names}"
                names=
                for tmp in ${tmps}; do
                    tmp2=${tmp}_NotOn
                    names="${names} $tmp2"
                done ;;
        esac
    }
    [ "`echo $opt | grep 'ChargeType'`" ] && {
        case $opt in
            ChargeType)
                tmps="${names}"
                names=
                for tmp in ${tmps}; do
                    tmp1=${tmp}_Mull
                    tmp2=${tmp}_Low
                    names="${names} $tmp1 $tmp2"
                done ;;
            ChargeType=Mull)
                tmps="${names}"
                names=
                for tmp in ${tmps}; do
                    tmp2=${tmp}_Mull
                    names="${names} $tmp2"
                done ;;
            ChargeType=Low)
                tmps="${names}"
                names=
                for tmp in ${tmps}; do
                    tmp2=${tmp}_Low
                    names="${names} $tmp2"
                done ;;
        esac
    }
    [ "`echo $opt | grep 'LocMet'`" ] && {
        tmpLoc=${opt:7}
        IFSBACK=$IFS
        IFS=,
        tmpsLoc=(${tmpLoc})
        IFS=$IFSBACK
        tmps="${names}"
        names=
        for tmp in ${tmps}; do
            for tmpLoc in ${tmpsLoc}; do
                tmp1=${tmp}_${tmpLoc}
                names="${names} $tmp1"
            done
        done
    }
    
    [ $opt = newPMtramix ] && {
        tmps="${names}"
        names=
        angthresh="1e-4 1e-5 1e-6 1e-7"
        truncthresh="1e-1 1e-2 1e-3 1e-4"
        for tmp in ${tmps}; do
            for ang in ${angthresh}; do
                for trunc in ${truncthresh}; do
                    tmp1=${tmp}_PMtrunc${trunc}_PMang${ang}
                    names="${names} $tmp1"
                done
            done
        done
    }
    [ `echo $opt | grep moread-` ] && {
        tmps="${names}"
        names=
        for tmp in ${tmps}; do
            tmp2=${tmp}_${opt}
            names="${names} $tmp2"
        done
    }
    count=`expr "$count" + 1`
done
echo ${names}
