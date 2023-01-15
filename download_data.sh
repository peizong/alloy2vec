#!/bin/bash
  
#download the model
wget https://www.dropbox.com/s/tzl2zxzigbk2o9i/model_121520
wget https://www.dropbox.com/s/tibgnb2higuzwca/model_121520.trainables.syn1neg.npy
wget https://www.dropbox.com/s/zj1uw4mlka6y2zx/model_121520.wv.vectors.npy
wget https://www.dropbox.com/s/ashco4x5wccc5kl/model_121520_phraser.pkl
mv model_121520* alloy2vec/training/models/

#download designed HEAs of 6 components
wget https://www.dropbox.com/s/g196rrf56nthrt4/sys_sim6.csv
mv sys_sim6.csv alloy2vec/postprocessing/contextSimilarity/parallel_version/
