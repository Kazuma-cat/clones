#!/usr/bin/env nix-shell
#!nix-shell -i bash -p qchem-2009.molcas
#
#SBATCH -c4
#SBATCH -t 1-0:00:00
#SBATCH -J MOLCAS
#SBATCH --mem-per-cpu=5GB

export MOLCAS_WORKDIR=$TMPDIR
export MOLCAS_MEM=20000

export PARNODES=$SLURM_CPUS_PER_TASK

iname=$SLURM_JOB_NAME

cp * $TMPDIR

cd $TMPDIR
JOBNAME=
pymolcas -b 1 -f $JOBNAME.input 

wait
mkdir $SLURM_SUBMIT_DIR/output
cp -r * $SLURM_SUBMIT_DIR/output/
