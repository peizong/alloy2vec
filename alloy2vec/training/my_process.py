from alloy2vec.processing import process
#mtp = process.MaterialsTextProcessor()

mtp = process.MaterialsTextProcessor()
def get_sentences(path):
  sentences,processed_sentences=[],[]
  with open(path, 'r',encoding="utf-8") as reader:
    for line in reader:
      sentences.append(line)
      #print("sentence i: ",line)
#mtp = process.MaterialsTextProcessor()
 # for sentence in sentences:
      processed=mtp.process(line, normalize_materials=True, convert_num=True,  
                         exclude_punct=True, make_phrases=True)
      #print("processed sentence i: ",processed)
      processed_sentences.append(processed[0])
  return processed_sentences

if __name__=="__main__":
  #path="data/acta_materialia_2018_abstracts.txt_shorter"
  path="data/all_abstracts_11_29.dat"
  sentences=get_sentences(path)
  #print(sentences)
