#!/bin/bash

#download the model
wget https://www.dropbox.com/s/m2mcobi8uw29r1c/model_121520
wget https://www.dropbox.com/s/tibgnb2higuzwca/model_121520.trainables.syn1neg.npy
wget https://www.dropbox.com/s/8bz4h2dia7eop6h/model_121520.trainables.syn1.npy
wget https://www.dropbox.com/s/zj1uw4mlka6y2zx/model_121520.wv.vectors.npy
wget https://www.dropbox.com/s/ashco4x5wccc5kl/model_121520_phraser.pkl
mv model_121520* alloy2vec/training/models/

#download pkl file
wget https://www.dropbox.com/s/ashco4x5wccc5kl/model_121520_phraser.pkl
mkdir alloy2vec/processing/models
mv model_121520_phraser.pkl alloy2vec/processing/models/phraser.pkl

#download designed HEAs of 6 components
wget https://www.dropbox.com/s/g196rrf56nthrt4/sys_sim6.csv
mv sys_sim6.csv alloy2vec/postprocessing/contextSimilarity/parallel_version/
