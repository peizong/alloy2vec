
import json
from collections import OrderedDict
from gensim.parsing.preprocessing import remove_stopwords,strip_punctuation
import numpy as np

def remove_stopword_punctuations(text):
  no_stopword = remove_stopwords(text)
  filtered_sentence=strip_punctuation(no_stopword)
  return filtered_sentence
def write(abstracts,filename):
  with open(filename,'a+',encoding="utf-8") as fw:
    for i in range(len(abstracts)):
      #filtered_abstract=remove_stopword_punctuations(str(abstracts[i]))
      #fw.write(str(filtered_abstract)+'\n')
      fw.write(str(abstracts[i])+'\n') #,encoding="utf-8")
    fw.close()
def extract_abstract_all(json_dir):
  corpus=[]
  corpus_unique_doi=[]
  dois=[]
  dois_unique=[]
  with open(json_dir,encoding="utf-8") as f:
    for jsonObj in f:
      entry = json.loads(jsonObj)['entry']
      abstract = dict(eval(entry))['description']
      corpus.append(abstract)
      #cited=dict(eval(entry))['citedby_count']
      #print(cited)
      #journal=dict(eval(entry))['publicationName']
      #print(journal)
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
  return corpus,corpus_unique_doi, dois, dois_unique
def extract_abstract_double_materials(json_dir,journals):
  corpus=[]
  corpus_unique_doi=[]
  dois=[]
  dois_unique=[]
  with open(json_dir,encoding="utf-8") as f:
    for jsonObj in f:
      entry = json.loads(jsonObj)['entry']
      abstract = dict(eval(entry))['description']
      corpus.append(abstract)
      #cited=dict(eval(entry))['citedby_count']
      #print(cited)
      journal=dict(eval(entry))['publicationName']
      #print(journal)
      data = dict(eval(entry))['coverDate']
      doi = dict(eval(entry))['doi']
      dois.append(doi)
      #print(abstract)
      #print(data)
      if doi not in dois_unique:
        if str(abstract) != 'None':
          dois_unique.append(doi)
          corpus_unique_doi.append(abstract)
        if journal in journals:
          dois_unique.append(doi)
          corpus_unique_doi.append(abstract)
  return corpus,corpus_unique_doi, dois, dois_unique
def init_list_of_objects(size):
    list_of_objects = list()
    for i in range(0,size):
        list_of_objects.append( list() ) #different object reference each time
    return list_of_objects
def extract_abstract_time(json_dir,years):
  corpus=[]
  dois=[]
  dois_unique=[]
  dois_unique_years=init_list_of_objects(len(years))
  corpus_unique_doi_years=init_list_of_objects(len(years))
  #corpus_unique_doi_years.append([np.zeros(1,len(years))])
  #dois_unique_years.append([np.zeros(1,len(years))])
  with open(json_dir,encoding="utf-8") as f:
    print("f: ",f)
    for jsonObj in f:
      entry = json.loads(jsonObj)['entry']
      abstract = dict(eval(entry))['description']
      corpus.append(abstract)
      #cited=dict(eval(entry))['citedby_count']
      #print(cited)
      data = dict(eval(entry))['coverDate']
      year=data[0:4]
      print("year ",year)
      doi = dict(eval(entry))['doi']
      dois.append(doi)
      #print(abstract)
      #print(data)
      if doi not in dois_unique:
        if str(abstract) != 'None':
          dois_unique.append(doi)
        #  corpus_unique_doi.append(abstract)
        if year in years:
          index=years.index(year)
          #print("index ",index,corpus_unique_doi_years)
          corpus_unique_doi_years[index].append(abstract)
          dois_unique_years[index].append(doi)
          #corpus_unique_doi.append(abstract)
        if int(year) < int(years[0]):
          index=0
          corpus_unique_doi_years[index].append(abstract)
          dois_unique_years[index].append(doi)
  #for index in range(len(years)):
  #  corpus_unique_doi_years[index].pop(0)
  return corpus,dois, dois_unique_years,corpus_unique_doi_years
def extract_authors_keywords_citations(json_dir,years,keyword):
  citations=[]
  dois=[]
  dois_unique=[]
  dois_unique_years=init_list_of_objects(len(years))
  citations_unique_doi_years=init_list_of_objects(len(years))
  with open(json_dir,encoding="utf-8") as f:
    for jsonObj in f:
      entry = json.loads(jsonObj)['entry']
      abstract = dict(eval(entry))['description']
      #corpus.append(abstract)
      cited=dict(eval(entry))['citedby_count']
      #print(cited)
      citations.append(cited)
      data = dict(eval(entry))['coverDate']
      year=data[0:4]
      #print("year ",year)
      doi = dict(eval(entry))['doi']
      dois.append(doi)
      title = dict(eval(entry))['title']
      keywords= dict(eval(entry))['authkeywords']
      #print("title, type(title): ", title, type(title), str(title))
      if str(title) != 'None' and str(keywords) == 'None':
        title = title.lower()
        keywords = title.split()
        keywords =[i.strip().lower() for i in keywords]
        #print("title, type(title): ", keywords, type(keywords), str(keywords))
      elif str(title) == 'None' and str(keywords) != 'None':
        keywords=keywords.lower()
        keywords=keywords.split('|')
        keywords =[i.strip().lower() for i in keywords]
      elif str(title) != 'None' and str(keywords) != 'None':
        keywords=keywords.lower()
        keywords=keywords.split('|')
        title = title.lower()
        keywords += title.split()
        keywords =[i.strip().lower() for i in keywords]
      else:
        keywords = [' ']
      #print(title.split(),keywords.split('|'))
      #else: keywords = title.split()
      #print(keywords)
      if doi not in dois_unique:
        if str(abstract) != 'None':
          dois_unique.append(doi)
        if year in years:
          index=years.index(year)
          #print("index ",index,corpus_unique_doi_years)
          #print("check keyword ", keyword[0] == any(keywords), keyword[0], any(keywords))
          keyword_logic=[x for x in keyword if x in keywords]
          #print("keyword logic,keyword,keywords: ",keyword_logic,keyword,keywords)
          if keyword_logic != []:
            citations_unique_doi_years[index].append(cited)
            dois_unique_years[index].append(doi)
        if int(year) < int(years[0]):
          index=0
          if any(keyword) == any(keywords):
            citations_unique_doi_years[index].append(cited)
            dois_unique_years[index].append(doi)
  return citations,dois, dois_unique_years,citations_unique_doi_years
if __name__=="__main__":
  corpus_unique_doi, dois, dois_unique=extract_abstract_all(json_dir)

  print("Total #dois: ",len(dois))
  new = list(set(dois)) 
  print("Unique #dois: ",len(new))

  print("use set funtion")
  print("Total #abstracts: ",len(corpus))
  write(corpus,'all_abstracts_11_29.dat') #,encoding="utf-8")
  new = list(set(corpus))
  print("Unique #abstracts: ",len(new))

  print("use dos screening for unique")
  print("Unique #dois: ",len(dois_unique))
  print("Unique #abstracts: ",len(corpus_unique_doi))
  write(corpus_unique_doi,'all_abstracts_doi_unique.dat') #,encoding="utf-8")
