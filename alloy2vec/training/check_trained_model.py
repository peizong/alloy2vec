#!/nfs/home/6/peiz/.conda/envs/text-mining/bin/python

from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import numpy as np
#default setting
from matplotlib import RcParams
#latex_style_times = RcParams({'font.family': 'serif',
#               'font.serif': ['Times'],
#               'text.usetex': True,
#               'axes.linewidth':2.0
#               #'figsize':[6.4,4.8]
#               })

#plt.style.use(latex_style_times)
plt.rcParams.update({'font.size': 14})
plt.rcParams["figure.figsize"]=[6.4,4.8]
plt.rcParams["figure.dpi"]=300

#w2v_model = Word2Vec.load("models/model_Oct2")
#model="models/pretrained_embeddings"
model="models/model_121520"
#model="models/model_121520"
w2v_model = Word2Vec.load(model) #("models/"+model) #pretrained_embeddings")
#---------check most similar words in formular a-b+c=?----------
check_similarity=True
if check_similarity==True:
  from alloy2vec.processing import MaterialsTextProcessor
  text_processor = MaterialsTextProcessor()
  b=w2v_model.wv.most_similar(
    positive=["cubic", text_processor.normalized_formula("Cu")],
    negative=[text_processor.normalized_formula("Zn")], topn=10)
  print(b)
#-------------------------------------------
check_similarity_topn=False #True
if check_similarity_topn==True:
  from alloy2vec.processing import MaterialsTextProcessor
  text_processor = MaterialsTextProcessor()
  word=text_processor.normalized_formula("thermoelectric") #CoCrFeMnNi")
  #word="high_entropy"
  #word="mechanical"
  #word="thermoelectric"
  #word="Al" #"Mn" #"Fe"
  # how to statistically show the trend of a field?
  #word="high-entropy"
  print(word)
  a=w2v_model.wv.most_similar(word,topn=20) #200
  word_candidates,cosine_similarity=[],[]
  print(a)
  for i in range(0,20): #len(a)):
    word_candidates.append(a[i*1][0])
    cosine_similarity.append(a[i*1][1])
  word_num=np.arange(len(word_candidates))
  fig, ax = plt.subplots()
  ax.barh(word_num, cosine_similarity,color='blue', align='center') #color='#0504aa',
  ax.set_yticks(word_num)
  ax.set_yticklabels(word_candidates)
  ax.invert_yaxis()  # labels read top-to-bottom
  plt.xlim((0.4,0.95))
  ax.set_xlabel('cosine similarity')
  ax.set_title('Ranking of cosine similarity for'+' "'+word+'"')
  #plt.savefig(word+"_"+model+".png",dpi=300)
  #plt.show()

  #print(word_candidates,cosine_similarity)

  #w2v_model.wv.most_similar("band_gap", topn=5)
