
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
import numpy as np
#w2v_model = Word2Vec.load("models/model_pei")
#w2v_model = Word2Vec.load("models/model_acta")
#w2v_model = Word2Vec.load("models/model_acta99_19")
model = Word2Vec.load("models/model_Yin")

#model = gensim.models.Word2Vec.load_word2vec_format(model_path, binary=True)
with open( 'tensorsfp', 'w+') as tensors:
    with open( 'metadatafp', 'w+') as metadata:
         for word in model.wv.index2word:
           encoded=word #word.encode('utf-8')
           #print(encoded)
           metadata.write(encoded + '\n')
           vector_row = '\t'.join(map(str, model[word]))
           tensors.write(vector_row + '\n')
