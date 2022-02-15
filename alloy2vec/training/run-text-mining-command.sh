#!/bin/env bash

time python phrase2vec.py -hs -sg --epochs=30 \
        --corpus=../../processing/raw-data-processing/materials_abstracts_121520.dat \
        --model_name=model_121520

#time python phrase2vec.py -hs -sg --epochs=30 \
#	--corpus=../../processing/raw-data-processing/materials_short.dat \
#        --model_name=model_short

