#!/bin/csh
## Change into the current working directory
#$ -cwd


#SBATCH --tasks=40

#SBATCH --tasks-per-node=40
#SBATCH --qos=long

module load  intelmpi/2019.0.117
module load  intel/2019.0.045
module load  vasp/5.4.4
##Run the parallel job
#mpirun vasp > output
#python seperate-abstracts.py
#time python read_process_json_abstract.py # > corpus-raw.dat
#time python main_read_process_abstract.py
#time python main_read_process_abstract.py "time"
#python main_read_process_abstract.py "all"
time python main_read_process_abstract.py "materials"
#time python main_read_process_abstract.py "citations"
