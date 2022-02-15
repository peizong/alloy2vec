#!/bin/bash
#SBATCH --nodes=1  
#SBATCH --ntasks-per-node=48
##SBATCH --cpus-per-task=48
#SBATCH --time=168:00:00
#SBATCH --mem=180GB
##SBATCH --job-name=tf-train
##SBATCH --output=tf-train.out
##SBATCH --gres=gpu:1


##!/bin/csh
## Change into the current working directory
##$ -cwd
##SBATCH --tasks=40
##SBATCH --tasks-per-node=40
##SBATCH --qos=long

#module load  intelmpi/2019.0.117
#module load  intel/2019.0.045
#module load  vasp/5.4.4
##Run the parallel job
#mpirun vasp > output
#python seperate-abstracts.py
#time python read_process_json_abstract.py # > corpus-raw.dat
#time python main_read_process_abstract.py
singularity exec --nv --overlay /scratch/zp2137/text-mining/overlay-25GB-500K.ext3:ro \
        /scratch/work/public/singularity/cuda11.2.2-cudnn8-devel-ubuntu20.04.sif \
        /bin/bash -c "source /ext3/env.sh; conda activate py36; ./run-text-mining-command.sh"
#time python main_read_process_abstract.py "time"
#time python main_read_process_abstract.py "all"
#time python main_read_process_abstract.py "materials"
#time python main_read_process_abstract.py "citations"
