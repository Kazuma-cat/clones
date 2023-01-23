#!/usr/bin/env nix-shell

filelist=()
recname=`realpath $0`
date | tee -a ~/record/sbatchlog.rec $recname
pwd | tee -a ~/record/sbatchlog.rec $recname
for file in ${filelist[@]}; do
    echo "sbatch $file.sh" | tee -a ~/record/sbatchlog.rec $recname
    sbatch $file.sh | tee -a ~/record/sbatchlog.rec $recname
    echo '' | tee -a sbatchlog ~/record/sbatchlog.rec $recname
done
