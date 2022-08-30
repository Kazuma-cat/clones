#!/bin/bash
#PBS -M miinosuke2@gmail.com -j oe
cd $PBS_O_WORKDIR

JOBNAMES=

# In the input directory, you provide
# - $JOBNAME.inp        # input file
# - $JOBNAME.xyz        # input xyz file   (optional)
# - $JOBNAME.ini.gbw    # initial orbitals (optional)

for JOBNAME in ${JOBNAMES}; do
    OUTFILE=$JOBNAME.out
    SCRDIR=$TMPDIR/$JOBNAME
    
    cp $PBS_NODEFILE $JOBNAME.nodes
    
    runorca $JOBNAME $TMPDIR >& $OUTFILE
    
    cp $SCRDIR/$JOBNAME.gbw .
done
