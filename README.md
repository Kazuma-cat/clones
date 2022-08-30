# name

# Demo

# Feature

'clones' generates orz input files modified its option, .sh file to submit orz Inputs to each nodes and Executable 'qsub.sh' file, which run all of .sh file with specifying the node which accepts each .sh file.

# Requirement

# Installation

# Usage

Please fill options in 'testinp' file and run ~/clones/main.sh. Orz inputs are generated from each line of 'testinp'.

How to write in eacf line of 'testinp'
[Molecular Name] [option1 option2 ... optionN]

You can modify all file to be generate by entering by enetering option after single !
! [option applied to all file to be generated]

The line including '!!' will be skipped

Acceptable option after '!'
* Dir=...        : determine directory where files are expanded : default=./
* OrzVer=        : determine the version of orz (you have to write the name of first directory of orz) : default=saitow-orz_temp
* fillnode=(y/n) : determine whether you allow .sh files to be submitted to the same node or not
* ncopy=         : !! under construction
* OmitOptPos=[\d,\d,...,\d] : you can omit a part of filename
* usecore=[\d]   : determine the number of node's core used to calculate
* n_node=[\d]    : determine the number of node used to calculate
* genechk=[y/n]  : determine whether generating genechk.sh or not

# Note

# Author

* Kazuma

# License