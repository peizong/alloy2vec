#!/bin/csh
## Change into the current working directory
#$ -cwd


#SBATCH --tasks=40

#SBATCH --tasks-per-node=40

module load  intelmpi/2019.0.117
module load  intel/2019.0.045
module load  vasp/5.4.4
##Run the parallel job
#mpirun vasp > output
python seperate-abstracts.py
