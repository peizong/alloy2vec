
import json
from collections import OrderedDict
from gensim.parsing.preprocessing import remove_stopwords,strip_punctuation

#json_dir='abstracts-8-21-20p.json'
json_dir='raw-data/'
json_dir +='abstracts-8-21-20.json'
#json_dir='abstracts-9-9-20.json'
#json_dir='abstracts-10-02-20.json'
#json_dir='abstracts-11-29-20_cleaned_nodup.json'

print(json_dir)

def remove_stopword_punctuations(text):
  no_stopword = remove_stopwords(text)
  filtered_sentence=strip_punctuation(no_stopword)
  return filtered_sentence
def write(abstracts,filename):
  with open(filename,'a+') as fw:
    for i in range(len(abstracts)):
      #filtered_abstract=remove_stopword_punctuations(str(abstracts[i]))
      #fw.write(str(filtered_abstract)+'\n')
      fw.write(str(abstracts[i])+'\n')
    fw.close()

corpus=[]
corpus_unique_doi=[]
dois=[]
dois_unique=[]

with open(json_dir) as f:
  for jsonObj in f:
    entry = json.loads(jsonObj)['entry']
    abstract = dict(eval(entry))['description']
    corpus.append(abstract)
    cited=dict(eval(entry))['citedby_count']
    print(cited)
    journal=dict(eval(entry))['publicationName']
    print(journal)
    data = dict(eval(entry))['coverDate']
    doi = dict(eval(entry))['doi']
    dois.append(doi)
    #print(abstract)
    #print(data)
    if doi not in dois_unique:
      if str(abstract) != 'None':
    #  print(doi,dois)
        dois_unique.append(doi)
        corpus_unique_doi.append(abstract)

print("Total #dois: ",len(dois))
new = list(set(dois)) 
print("Unique #dois: ",len(new))

print("use set funtion")
print("Total #abstracts: ",len(corpus))
write(corpus,'all_abstracts_11_29.dat')
new = list(set(corpus))
print("Unique #abstracts: ",len(new))

print("use dos screening for unique")
print("Unique #dois: ",len(dois_unique))
print("Unique #abstracts: ",len(corpus_unique_doi))
write(corpus_unique_doi,'all_abstracts_doi_unique.dat')
