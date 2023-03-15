#!/run/current-system/sw/bin/bash
filelist=()
rootchkx=/home/20/kazuma/clones/chkx2/
tmpchkx=$rootchkx
for filename in ${filelist[@]}; do
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
            extn=RasOrb
            savename=${filename%%_*}
            savename=${savename#cbl-};savename=${savename#cbi-}
            logname=${tmpchkx}/${chkxlist[$nchkx]}
            #logname=${logname#/home/20/kazuma/clones/chkx2/}
            logname=${logname#$rootchkx}
            logname=${logname//'/'/'-'}
            logname=${logname##'-*'}
            echo ${tmpchkx}/${chkxlist[$nchkx]}
            echo "logname = ${logname}"
            read -p 'Is this correct? (y/n)' tmp
            [ x$tmp != xy ] && continue
            cp -i ${filename}.$extn ${tmpchkx}/${chkxlist[$nchkx]}/${savename}.$extn
            [ $? ] && echo "save as ${rootchkx}/${chkxlist[$nchkx]}/${savename}.$extn" | tee -a ~/record/genechk.rec
            # record information --------------
            [ -e ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log ] || touch ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
            date >> ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
            #echo "${tmpchkx}/${chkxlist[$nchkx]}/${filename}.chkx" >> ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
            echo "`pwd`/${filename}.$extn" >> ${tmpchkx}/${chkxlist[$nchkx]}/${logname}.log
            break
        elif [ a$nodir = afalse ]; then
            #echo "$tmpchkx"
            #echo ${chkxlist[$nchkx]}
            tmpchkx=$tmpchkx/${chkxlist[$nchkx]}
            continue
        fi
    done
done
