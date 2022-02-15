
import gensim
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
common_dictionary = Dictionary(common_texts)
common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]

corpus=common_corpus #"../data/all_abstracts_11_29.dat"
lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           #id2word=id2word,
                                           num_topics=20, 
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
# Print the Keyword in the 10 topics
print(lda_model.print_topics())
doc_lda = lda_model[corpus]

