
import json
from collections import OrderedDict
from gensim.parsing.preprocessing import remove_stopwords,strip_punctuation
from fun_read_process_abstract import *
import sys

json_dir='raw-data/'
#json_dir+='abstracts-8-21-20p.json'
#json_dir +='abstracts-8-21-20.json'
#json_dir+='abstracts-9-9-20.json'
#json_dir+='abstracts-10-02-20.json'
#json_dir+='abstracts-11-29-20_cleaned_nodup.json'
json_dir +='abstracts-12-15-20-all.json'
#json_dir +='abstracts-jac-msea-aem-am-1999-2019.json'
print(json_dir)

def print_meta_data(corpus,dois_unique,corpus_unique_doi,filename):
  print("Total #abstracts: ",len(corpus))
  write(corpus,filename+'_abstracts_11_29.dat')

  print("Unique #dois: ",len(dois_unique))
  print("Unique #abstracts: ",len(corpus_unique_doi))
  write(corpus_unique_doi,filename+'_abstracts_doi_unique.dat')
  return None

def print_meta_data_years(corpus,dois_unique_years,corpus_unique_doi_years,filename,years):
  #print("Total #abstracts: ",len(corpus))
  #write(corpus,filename+'_abstracts_11_29.dat')

  for index in range(len(years)):
    print("Year: ",years[index])
    print("Unique #dois: ",len(dois_unique_years[index]))
    print("Unique #abstracts: ",len(corpus_unique_doi_years[index]))
    write(corpus_unique_doi_years[index],"years/"+filename+'_'+years[index]+'_abstracts_doi_unique.dat')
  return None
def print_meta_data_citations(citations,dois_unique_years,citations_unique_doi_years,filename,years):
  for index in range(len(years)):
    print("Year: ",years[index])
    print("Unique #dois: ",len(dois_unique_years[index]))
    print("Unique #papers: ",len(citations_unique_doi_years[index]))
    #info=citations_unique_doi_years[index]+"	"+dois_unique_years[index]
    #write(info,"citations/"+filename+'_'+years[index]+'_citations_doi_unique.dat')
    write(citations_unique_doi_years[index],"citations/"+filename+'_'+years[index]+'_citations_doi_unique.dat') #,encoding="utf-8")
    write(dois_unique_years[index],"citations/"+filename+'_'+years[index]+'_dois_unique.dat') #,encoding="utf-8")
  return None
if __name__=="__main__":

  if sys.argv[1]=="all":
    print("all unique abstract")
    filename=sys.argv[1]
    corpus,corpus_unique_doi, dois, dois_unique=extract_abstract_all(json_dir)
    print_meta_data(corpus,dois_unique,corpus_unique_doi,filename)
  if sys.argv[1]=="materials":
    print("all abstracts of materials journals are replicate")
    filename=sys.argv[1]
    journals=["Acta Materialia", "Scripta Materialia", "Materials and Design", "Journal of Alloys and Compounds", "Materials Science and Engineering A: Structural Materials: Properties, Microstructure and Processing", "Intermetallics", "Metallurgical and Materials Transactions A", "Annual Review of Materials Research", "Progress in Materials Science", "Science", "Nature", "Nature Reviews Materials","Physical Review Materials", "Advanced Materials", "Advanced Engineering Materials", "International Journal of Plasticity", "Current Opinion in Solid State and Materials Science", "Journal of Materials Science and Technology"]
    corpus,corpus_unique_doi, dois, dois_unique=extract_abstract_double_materials(json_dir,journals)
    print_meta_data(corpus,dois_unique,corpus_unique_doi,filename)
  if sys.argv[1]=="time":
    print("corpa are classificed by time/year")
    filename=sys.argv[1]
    years=["2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
    corpus,dois,dois_unique_years,corpus_unique_doi_years=extract_abstract_time(json_dir,years)
    print_meta_data_years(corpus,dois_unique_years,corpus_unique_doi_years,filename,years)
  if sys.argv[1]=="citations":
    print("citations are classificed by time/year")
    filename=sys.argv[1]
    #years=["2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018"]
    #keywords=['hydrogel','Pei']
    years=["2014","2015"]
    keywords=['high entropy alloys','high-entropy alloys','high entropy alloy','high-entropy alloy','multicomoponent','concentrated alloys','concentrated alloy','complex concentrated','compositionally complex','concentrated solid solutions','concentrated solid solution']
    citations,dois,dois_unique_years,citations_unique_doi_years=extract_authors_keywords_citations(json_dir,years,keywords)
    print_meta_data_citations(citations,dois_unique_years,citations_unique_doi_years,filename,years)
