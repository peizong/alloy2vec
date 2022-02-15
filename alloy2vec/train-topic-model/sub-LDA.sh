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
#./train_model.sh
#./train_model2018.sh

#time python phrase2vec.py -hs -sg --epochs=30 --corpus=data/all_abstracts_11_29.dat --model_name=model_11_29_20
python run-LDA.py

#python phrase2vec.py --corpus=data/acta-materialia-1999-2019-abstracts.txt --model_name=model_acta99_19
#python phrase2vec.py --corpus=data/acta-materialia-2018-abstracts.txt --model_name=model_acta

#time python phrase2vec.py -hs -sg --epochs=30  --corpus=data/mat2vec-1a5b3240-abstracts.csv --model_name=model_Yin2
#time python phrase2vec.py --epochs=50  --corpus=data/mat2vec-1a5b3240-abstracts.csv --model_name=model_Yin2_no_hs_sg
#time python phrase2vec.py -hs -sg --epochs=50 --corpus=data/complete-corpus-raw.dat --model_name=model_John_50
#time python phrase2vec.py -hs -sg -keep_formula -notmp --epochs=30 --corpus=data/all_abstracts_doi_unique.dat --model_name=model_Oct2_2
