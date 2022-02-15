from gensim.parsing.preprocessing import remove_stopwords,strip_punctuation
from mat2vec.processing import process
from gensim import corpora
from tqdm import tqdm
#mtp = process.MaterialsTextProcessor()

def test_process(sentences):
    mtp = process.MaterialsTextProcessor()
    # test data
    matnorm = [True, True, True, True, False]
    convert_nums = [True, True, True, False, True]
    exclude_punct = [True, True, True, True, False]
    make_phrases = [True, True, True, False, True]

    materials = [
        [("Ni(CO)4", "C4NiO4")],
        [("Ni(CO)4", "C4NiO4")],
        [("Ni(CO)4", "C4NiO4")],
        [("iron", "Fe")],
        [("iron", "Fe")]
    ]
    # running the tests
    for s, mn, cn, ep, mp in zip(
            sentences, matnorm, convert_nums, exclude_punct, make_phrases):
        #print("s: ", s)
        proc, mats = mtp.process(
            s, normalize_materials=mn, convert_num=cn, exclude_punct=ep, make_phrases=mp)
    return proc, mats
def remove_stopword_punctuations(text):
  no_stopword = remove_stopwords(text)
  filtered_sentence=strip_punctuation(no_stopword)
  return filtered_sentence

sentences=[]
with open('acta_materialia_2018_abstracts.txt_shorter', 'r') as reader:
  for line in reader:
    #new_line=remove_stopword_punctuations(line)
    #print(new_line,line)
    sentences.append([line])
#corpus=open('acta_materialia_2018_abstracts.txt_shorter')
#print(corpus.readlines())
#sentences=corpus
for sentence in sentences:
  print(sentence)
  processed=test_process(sentence)
  print(processed)
mtp = process.MaterialsTextProcessor()
processed2=mtp.process(
            sentences[2], normalize_materials=True, convert_num=True, exclude_punct=True, make_phrases=True)
#print(processed2)
#corpus = corpora.textcorpus.TextCorpus.get_texts('acta_materialia_2018_abstracts.txt_shorter')
#print(corpus)
#for line in corpus:
#    print(line)
