
import json
from collections import OrderedDict

json_dir='abstracts-8-21-20.json'
corpus=[]
with open(json_dir) as f:
  for jsonObj in f:
    abstractDict=json.loads(jsonObj) #,object_pairs_hook=OrderedDict)
    corpus.append(abstractDict)
#  data = json.load(f)

decoder = json.JSONDecoder(object_pairs_hook=OrderedDict)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
i=0
for abstract_i in corpus: 
  i +=1
  print(abstract_i["entry"]) #'description']) 
  abstract=json.loads(abstract_i["entry"])
  print(abstract['description'])
  if i>0:break
#print(data)
