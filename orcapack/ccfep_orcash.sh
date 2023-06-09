#!/bin/sh
#PBS -l select=1:ncpus=x:mpiprocs=x:ompthreads=x
#PBS -l walltime=12:00:00

if [ ! -z "${PBS_O_WORKDIR}" ]; then
  cd "${PBS_O_WORKDIR}"
fi

. /apl/orca/5.0.4/orca_env.sh
orca=/apl/orca/5.0.4/orca/orca

JOBNAME=
INPUT=$JOBNAME.inp
OUTPUT=$JOBNAME.out

# do not use local disk. it might be slower somewhat.

$orca ${INPUT} > ${OUTPUT}
