#!/bin/bash
#PBS -M miinosuke2@gmail.com -j oe
cd $PBS_O_WORKDIR

# How to submit: qsub -l nodes=2:ppn=6:qj -v OMP=3 h2o.sh

MOLNAME=
ncopy=

export OMP_NUM_THREADS=1
if [ x$OMP != x ]; then
    export OMP_NUM_THREADS=$OMP  # <= set num threads
fi

# calc NP and PPN
NP=$(( $PBS_NP / $OMP_NUM_THREADS ))
PPN=$(( $PBS_NUM_PPN / $OMP_NUM_THREADS ))

# In the input directory, you provide
# - $JOBNAME.py         # input file
# - $JOBNAME.chkx       # checkpoint file

echo PBS_NP=$PBS_NP, PBS_NUM_PPN=$PBS_NUM_PPN, NP=$NP, PPN=$PPN, OMP_NUM_THREADS=$OMP_NUM_THREADS
i=1
while [ i -le $ncopy ]; do
    JOBNAME=${MOLNAME}_${i}
    [ -e ${JOBNAME}.py ] || exit 1
    OUTFILE=$JOBNAME.out
    SCRDIR=$TMPDIR
    
    . ~yanai/orzconfig/gcc73.mvapich2.el75.2.sh
    
    export ORZSRC=
    export ORZOBJ=
    #export ORZSRC=~saitow/ORZ-PCM-OFFICIAL/orz
    #export ORZOBJ=~saitow/ORZ-PCM-OFFICIAL/orz/obj-opt
    
    export PYTHONPATH=$ORZSRC/src/pylib
    
    cp -f $JOBNAME.chkx $SCRDIR/. || echo no init chkx
    
    `eval echo $MPIRUNQ` $ORZOBJ/src/sci/scf/scf -w ${SCRDIR} $JOBNAME.py >& $JOBNAME.py.scf
    #`eval echo $MPIRUNQ` $ORZOBJ/src/sci/casscf/casscf -w ${SCRDIR} $JOBNAME.py >& $JOBNAME.py.casscf-pao
    #`eval echo $MPIRUNQ` $ORZOBJ/src/sci/icmr/icmr -w ${SCRDIR} $JOBNAME.py >& $JOBNAME.py.icmr
    `eval echo $MPIRUNQ` $ORZOBJ/src/sci/lct/lct -w ${SCRDIR} $JOBNAME.py >& $JOBNAME.py.lct
    
    # Fetch the information on MOs
    cp $SCRDIR/$JOBNAME.chkx .
    cp $SCRDIR/$JOBNAME.fchk .
    cp $SCRDIR/$JOBNAME.lct .
    cp $SCRDIR/$JOBNAME.loc-01.fchk .
    cp $SCRDIR/$JOBNAME.py ./${JOBNAME}_out.py
    i=`expr $i + 1`
done
