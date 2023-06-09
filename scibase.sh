#!/bin/sh
#PBS -l select=1:ncpus=4:mpiprocs=4:ompthreads=1
#PBS -l walltime=00:30:00

if [ ! -z "${PBS_O_WORKDIR}" ]; then
  cd "${PBS_O_WORKDIR}"
fi

. /apl/orca/5.0.4/orca_env.sh
orca=/apl/orca/5.0.4/orca/orca

INPUT=orca.inp
OUTPUT=orca.out

# do not use local disk. it might be slower somewhat.

$orca ${INPUT} > ${OUTPUT}
