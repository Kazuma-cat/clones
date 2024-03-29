#! /bin/bash
export ORZSRC=~kazuma/orzsource/orz-git/
export ORZOBJ=~kazuma/orzsource/orz-git/obj-opt
export PYTHONPATH=$ORZSRC/src/pylib
filelist=()
#rootchkx=~/clones/chkx
rootchkx=~/clones/chkx2
chkxdirs=
option=${1:-default}
for tmp in `ls -d ${rootchkx}/*`; do
    chkxdirs=("${chkxdirs} ${tmp}")
done
for filename in ${filelist[@]}; do
    case ${option} in
        inp)
            : ;;
        out)
            echo "previous 'filename' = ${filename}"
            cp ${filename}.py ${filename}_out.py
            filename=${filename}_out;;
        default)
            echo "please enter an argument"
            echo "available argument list : inp, out"
            exit 1 ;;
        *)
            echo "undefined argument detected"
            echo "available argument list : inp, out"
            exit 1 ;;
    esac
    #[ $option = 'out' ] && {
    #    echo "previous 'filename' = ${filename}"
    #    cp ${filename}.py ${filename}_out.py
    #    filename=${filename}_out
    #}
    echo "--------------------------------------"
    echo "          ${option} option            "
    echo "--------------------------------------"
    echo "filename: ${filename}"
    while : ;do
        read -p 'Do you reorder orbitals of this file?(y/n/c):' yn_reorder
        [ $yn_reorder = y ] && break
        [ $yn_reorder = n ] && break
        [ $yn_reorder = c ] && break
    done
    [ $yn_reorder = c ] && continue
    
    # reorder loop
    [ ${yn_reorder} = y ] && {
        # begin get information from file
        if [ "`grep '# info ...' $filename.py`" ]; then
            frozen_base=`grep 'icmr.frozen' $filename.py | grep -o '[0-9]\+'`
            closed_base=`grep '#log nclosed=' $filename.py | grep -o '[0-9]\+'`
            occ_base=`grep '#log nocc=' $filename.py | grep -o '[0-9]\+'`
        else
            frozen_base=`grep 'icmr.frozen' $filename.py | grep -o '[0-9]\+'`
            closed_base=`grep 'icmr.closed' $filename.py | grep -o '[0-9]\+'`
            occ_base=`grep 'icmr.occ' $filename.py | grep -o '[0-9]\+'`
        fi
        # end get information from file
        occ_base_d2=`expr $occ_base / 2`
        echo "occ_base_d2 = ${occ_base_d2}"
        frozen_base=${frozen_base%' .*'}
        closed_base=${closed_base%' .*'}
        closed_base=`echo $closed_base | sed 's/\s.*//g'`
        echo "icmr.frozen = $frozen_base"
        echo "icmr.closed = $closed_base"
        echo "icmr.occ    = $occ_base"
        orb_totalM1=`expr $frozen_base + $closed_base + $occ_base_d2 - 1`
        orb_total=`expr $frozen_base + $closed_base + $occ_base_d2`
        echo "The number of orbitals = $orb_total"
        echo "Max index of orbitals = $orb_totalM1"
        # enter occuppied active orbitals
        while : ;do
            read -p 'please enter number of occupied acitve orbitals (c:continue to next file):' occact
            [ ${#occact} = 1 ] && [ ${occact} = c ] && break
            for tmp2 in ${occact}; do
                expr "${tmp2}" > ~/null;
                [ $? -ge 2 ] && break;
            done
            expr "${tmp2}" > ~/null; [ $? -ge 2 ] && echo 'argument contains something except number. please enter again'
            expr "${tmp2}" > ~/null; [ $? -lt 2 ] && [ $tmp2 -ge 1 ] && [ $tmp2 -le $orb_total ] && break
            expr "${tmp2}" > ~/null; [ $? -lt 2 ] && [ $tmp2 -ge 1 ] && [ $tmp2 -gt $orb_total ] && echo 'argument is too large. please enter again'
        done
        [ ${#occact} = 1 ] &&[ $occact = c ] && continue

        # enter unoccuppied active orbitals
        while : ;do
            read -p 'please enter number of unoccupied acitve orbitals (c:continue to next file):' unoccact
            [ ${#unoccact} = 1 ] && [ ${unoccact} = c ] && break
            for tmp2 in ${unoccact}; do  expr "${tmp2}" > ~/null; [ $? -ge 2 ] && break; done
            expr "${tmp2}" > ~/null; [ $? -ge 2 ] && echo 'argument contains something except number. please enter again'
            expr "${tmp2}" > ~/null; [ $? -lt 2 ] && [ $tmp2 -ge 1 ] && [ $tmp2 -gt $orb_total ] && break
            expr "${tmp2}" > ~/null; [ $? -lt 2 ] && [ $tmp2 -ge 1 ] && [ $tmp2 -le $orb_total ] && echo 'argument is too small. please enter again'
            expr "${tmp2}" > ~/null; [ $? -lt 2 ] && [ $tmp2 -lt 1 ] && { echo 'negatieve number is detected. This process will continue but please note.'; virvac=y; break;}
        done
        # enter adding orbitals
        naddorb=0
        while : ; do
            read -p 'please enter number of adding orbitals (c:continue to next file):' naddorb
            [ ${#naddorb} = 0 ] && { echo '0 is used as naddorb';naddorb=0;break;}
            [ ${#naddorb} = 1 ] && {
                expr "${naddorb}" > ~/null; [ $? -ge 2 ] && echo 'argument contains something except number. please enter again'
                expr "${naddorb}" > ~/null; [ $? -lt 2 ] && break
            }
            [ ${#naddorb} != 1 ] && echo 'please enter only one argument' 
        done
        orb_total=`expr $orb_total + $naddorb`
        
        [ ${#unoccact} = 1 ] &&[ $unoccact = c ] && continue
        [ $virvac = y ] && unoccact=

        occact_M1_list=
        for tmp2 in ${occact}; do
            tmp3=`expr ${tmp2} - 1`
            occact_M1_list="${occact_M1_list}${tmp3},"
        done
        occact_M1_list=${occact_M1_list%,}

        fullact_list=
        for tmp2 in ${occact} ${unoccact}; do
            fullact_list="${fullact_list}${tmp2},"
        done
        fullact_list=${fullact_list%,}
        sed -i -e "s/casscf.maxMacroloop.*/# begin sorting\ncasscf.orbconfig = 'orblist'\ncasscf.frozen = [] # this part should be like this\ncasscf.closed = [(x) for x in range(0,${orb_total}) if not (x in [${occact_M1_list}])]  # incices of MOs that should be in closed space\ncasscf.occ    = [(x-1) for x in [${fullact_list}]] # indices of MOs that\n# end sorting\ncasscf.maxMacroloop = 100/g" ${filename}.py
        cp ${filename}.py ~/record/reorder_inp.py
        # s/casscf.maxMacroloop.*/# begin sorting
        # casscf.orbconfig = 'orblist'
        # casscf.frozen = [] # this part should be like this
        # casscf.closed = [(x) for x in range(0,${orb_total}) if not (x in [${occact_M1_list}])  # incices of MOs that should be in closed space
        # casscf.occ    = [(x-1) for x in [${fullact_list}]] # indices of MOs that
        # # end sorting
        #
        # casscf.maxMacroloop = 100

        #$ORZOBJ/src/sci/casscf/casscf_util -w /work/kazuma ${filename}.py sortinitialorbs
        $ORZOBJ/src/sci/casscf/casscf_util -w . ${filename}.py sortinitialorbs
        #cp ${filename}.py ${filename}.debug.py
        echo "----------------------------------------------------------------"
        sed -i -z -e "s/# begin sorting.*# end sorting//g" ${filename}.py

    } # end of reorder section

    # copy chkx file to chkx directory
    date | tee -a ~/record/genechk.rec
    echo -n "pwd = " | tee -a ~/record/genechk.rec
    pwd | tee -a ~/record/genechk.rec
    if [ $rootchkx = ~/clones/chkx ]; then
        echo '---------------------'
        echo '     old option      '
        echo '---------------------'
        while :
        do
            echo 'list of chkx directory'
            i=1
            chkxlist=()
            for chkxdir in ${chkxdirs[@]}; do
                tmp=`basename ${chkxdir}`
                chkxlist[$i]=$tmp
                echo "${i}:${tmp}"
                i=`expr $i + 1`
            done
            read -p 'please choose the number of chkx directory(c:skip):' nchkx
            expr ${nchkx} > ~/null; [ $? -ge 2 ] && { echo 'string is included in your input'; continue;}
            [ ${#nchkx} = 1 ] && [ ${nchkx} = c ] && break
            [ ${nchkx} -ge ${i} ] && { echo 'incorrect number is included in your input'; continue;}
            [ ${nchkx} -lt ${i} ] && {
                savename=${filename%%_*}
                cp -i ${filename}.chkx ${rootchkx}/${chkxlist[$nchkx]}/${savename}.chkx
                [ $? ] && echo "save as ${rootchkx}/${chkxlist[$nchkx]}/${savename}.chkx" | tee -a ~/record/genechk.rec
                # record information --------------
                [ -e ${rootchkx}/${chkxlist[$nchkx]}/${chkxlist[$nchkx]}.log ] || touch ${rootchkx}/${chkxlist[$nchkx]}/${chkxlist[$nchkx]}.log
                date >> ${rootchkx}/${chkxlist[$nchkx]}/${chkxlist[$nchkx]}.log
                echo "${rootchkx}/${chkxlist[$nchkx]}/${filename}.chkx" >> ${rootchkx}/${chkxlist[$nchkx]}/${chkxlist[$nchkx]}.log
                break
            }
        done
    elif [ $rootchkx = ~/clones/chkx2 ]; then
        echo '---------------------'
        echo '      new option     '
        echo '---------------------'
        tmpchkx=$rootchkx
        while :
        do
            i=1
            chkxlist=()
            for chkxdir in `ls $tmpchkx`; do
                tmp=`basename ${chkxdir}`
                chkxlist[$i]=$tmp
                echo "${i}:${tmp}"
                i=`expr $i + 1`
            done
            read -p 'Choose the index of chkx directory(c:skip):' nchkx
            expr ${nchkx} > ~/null; [ $? -ge 2 ] && { echo 'string is included in your input'; continue;}
            [ ${#nchkx} = 1 ] && [ ${nchkx} = c ] && break
            [ ${nchkx} -ge ${i} ] && { echo 'incorrect number is included in your input'; continue;}
            [ -d $tmpchkx/${chkxlist[$nchkx]} ] || { echo 'you must choose directory'; continue; }
            nodir=true
            for tmp in `ls $tmpchkx/${chkxlist[$nchkx]}`; do
                [ -d $tmpchkx/${chkxlist[$nchkx]}/$tmp ] && nodir=false
            done
            if [ a$nodir = atrue ]; then
                extn=chkx
                savename=${filename%%_*}
                savename=${savename#cbl-};savename=${savename#cbi-}
                logname=${tmpchkx}/${chkxlist[$nchkx]}
                logname=${logname#/home/20/kazuma/clones/chkx2/}
                logname=${logname//'/'/'-'}
                logname=${logname##'-*'}
                echo ${tmpchkx}/${chkxlist[$nchkx]}
                echo "logname = ${logname}"
                read -p 'Is this correct? (y/n)' tmp
                [ x$tmp != xy ] && continue
                cp -i ${filename}.$extn ${tmpchkx}/${chkxlist[$nchkx]}/${savename}.$extn
                [ $? ] && echo "save as ${rootchkx}/${chkxlist[$nchkx]}/${savename}.chkx" | tee -a ~/record/genechk.rec
                # record information --------------
                [ -e ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log ] || touch ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
                date >> ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
                #echo "${tmpchkx}/${chkxlist[$nchkx]}/${filename}.chkx" >> ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
                echo "`pwd`/${filename}.chkx" >> ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
                break
            elif [ a$nodir = afalse ]; then
                #echo "$tmpchkx"
                #echo ${chkxlist[$nchkx]}
                tmpchkx=$tmpchkx/${chkxlist[$nchkx]}
                continue
            fi
        done
    fi
done
        
