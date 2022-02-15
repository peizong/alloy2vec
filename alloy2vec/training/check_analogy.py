#!/nfs/home/6/peiz/.conda/envs/text-mining/bin/python
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import numpy as np
#default setting
from matplotlib import RcParams
#plt.style.use(latex_style_times)
plt.rcParams.update({'font.size': 6})
plt.rcParams["figure.figsize"]=[8,4.8]
plt.rcParams["figure.dpi"]=300
model="pretrained_embeddings"
#model="model_11_29_20" 
#model="model_Oct2"
w2v_model = Word2Vec.load("models/"+model) #pretrained_embeddings")
word="CoCrFeMnNi"
print(w2v_model.vocab[word].count)
#word="high-entropy"
#word="mechanical"
#word_sim=w2v_model.wv.most_similar(
#    positive=["helium", "Fe"], 
#    negative=["He"], topn=10)
from mat2vec.processing import MaterialsTextProcessor
text_processor = MaterialsTextProcessor()
norm_word=text_processor.normalized_formula("Co1Cr1Fe1Ni1Mn0.5")
print(norm_word)
word_sim=w2v_model.wv.most_similar(
    positive=["cubic", "CdSe"],
    negative=["GaAs"], topn=1)

#word_sim=w2v_model.wv.most_similar(
#    positive=["cubic", text_processor.normalized_formula("CdSe")], 
#    negative=[text_processor.normalized_formula("GaAs")], topn=1)
print(word_sim)
#word="XXOO" #"Mg"
# how to statistically show the trend of a field?
#word="high-entropy"

