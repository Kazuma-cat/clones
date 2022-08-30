#!/bin/bash
#PBS -M miinosuke2@gmail.com -j oe
cd $PBS_O_WORKDIR

JOBNAMES=
for JOBNAME in ${JOBNAMES}; do
    INP=${JOBNAME}.gjf
    export GAUSS_SCRDIR=$TMPDIR
    g16 $INP
    formchk $JOBNAME.chk
    babel -ifchk $JOBNAME.fchk -oxyz $JOBNAME.xyz
done
