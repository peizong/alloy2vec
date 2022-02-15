
import os,re,sys

# initializing bad_chars_list 
bad_chars = [';', ':', '!', '.', '(', ')', '"', "*"] 

#filename="mat2vec-1a5b3240-abstracts-head.csv"
filename=sys.argv[1] #"mat2vec-1a5b3240-abstracts.csv"
print(filename)

with open(filename,"r") as corpus:
  data=corpus.readlines()
  for line in data:
    words=line.split(',') #("	")
    split_again=str(words[0]).split(".")
    year=split_again[3]
    if int(year)>2020 or int(year)<1900:
      year=split_again[2]
    filename_i=os.path.join("corpus_by_year",str(year)+".csv")
    with open( filename_i, 'a+') as corpus_i:
      words_j=''
      for j in range(1,len(words)):
        words_j +=words[j]
      #words_jj=re.split('.|,|"|:', str(words_j))
      #words_k=''
      #for k in range(0,len(words_jj)):
      #  words_k += words_jj[k]
      # remove bad_chars  
      for ii in bad_chars : 
        words_j = words_j.replace(ii, '') 
      corpus_i.write(words_j + '\n')
