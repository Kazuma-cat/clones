#! /bin/bash
JOBNAME=$1
loctype=$2
frozen=`grep 'icmr.frozen' $JOBNAME.py | grep -o '[0-9]\+'`
closed=`grep 'icmr.closed' $JOBNAME.py | grep -o '[0-9]\+'`
occ=`grep 'icmr.occ' $JOBNAME.py | grep -o '[0-9]\+'`
frozen=${frozen%' .*'}
closed=${closed%' .*'}
occ=${occ%' .*'}
posfrozen=${frozen}
posclosed=`expr $frozen + $closed`
posocc=`expr $frozen + $closed + $occ`
#sed -i -e "s/casscf.maxMacroloop.*/# begin loc\ncasscf.orbconfig = 'orblist'\ncasscf.frozen = []\ncasscf.closed = range(0,$posfrozen) #closed-marking\ncasscf.occ = range($posclosed,$posocc)\n# end loc\ncasscf.maxMacroloop = 100/g" ${JOBNAME}.py

if [ $loctype = CA ]; then
    #new loc version
    sed -i -e "s/casscf.maxMacroloop.*/# begin loc\ncasscf.orbconfig = 'orblist'\ncasscf.frozen = []\ncasscf.closed = [] #closed-marking\ncasscf.occ = range($posfrozen,$posocc)\n# end loc\ncasscf.maxMacroloop = 100/g" ${JOBNAME}.py
    # #begin loc
    # casscf.orbconfig = "orblist"
    # casscf.frozen = []
    # casscf.closed = range(0,$frozen) #closed-marking
    # casscf.occ = range($closed,$occ)
    # #end loc
    # casscf.maxMacroloop = 100
    
    #$ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizeclosed >& $JOBNAME.py.iniloc1.tmp
    ##cp ${JOBNAME}.py ${JOBNAME}.tmp1.py
    #sed -i -e "s/.*#closed-marking/casscf.closed = range($posfrozen,$posclosed) #closed-marking/g" ${JOBNAME}.py
    #
    #$ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizeclosed >& $JOBNAME.py.iniloc2.tmp
    #$ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizeocc >& $JOBNAME.py.iniloc3.tmp
    ##cp ${JOBNAME}.py ${JOBNAME}.tmp2.py
    
    # new loc version
    $ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizeocc >& $JOBNAME.py.locCA
    sed -i -z -e "s/# begin loc.*# end loc//g" ${JOBNAME}.py
elif [ $loctype = DV ]; then
    posdomo=$(($posclosed + $occ / 2))
    sed -i -e "s/casscf.maxMacroloop.*/# begin loc\ncasscf.orbconfig = 'orblist'\ncasscf.frozen = range(0,$posfrozen)\ncasscf.closed = range($posfrozen,$posdomo) #closed-marking\ncasscf.occ = []\n# end loc\ncasscf.maxMacroloop = 100/g" ${JOBNAME}.py
    # #begin loc
    # casscf.orbconfig = "orblist"
    # casscf.frozen = range(0,$posfrozen)
    # casscf.closed = range($posfrozen,$posdomo) #closed-marking
    # casscf.occ = []
    # #end loc
    # casscf.maxMacroloop = 100
    $ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizeclosed >& $JOBNAME.py.locD
    $ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizevirtual >& $JOBNAME.py.locV
    sed -i -z -e "s/# begin loc.*# end loc//g" ${JOBNAME}.py
elif [ $loctype = nC ]; then
    sed -i -e "s/casscf.maxMacroloop.*/# begin loc\ncasscf.orbconfig = 'orblist'\ncasscf.frozen = range(0,$posfrozen)\ncasscf.closed =[] #closed-marking\ncasscf.occ = []\n# end loc\ncasscf.maxMacroloop = 100/g" ${JOBNAME}.py
    # #begin loc
    # casscf.orbconfig = "orblist"
    # casscf.frozen = range(0,$posfrozen)
    # casscf.closed = range($posfrozen,$posdomo) #closed-marking
    # casscf.occ = []
    # #end loc
    # casscf.maxMacroloop = 100
    #$ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizeclosed >& $JOBNAME.py.locD
    $ORZOBJ/src/sci/casscf/casscf_util -w ${SCRDIR} $JOBNAME.py localizevirtual >& $JOBNAME.py.locnC
    sed -i -z -e "s/# begin loc.*# end loc//g" ${JOBNAME}.py
fi
