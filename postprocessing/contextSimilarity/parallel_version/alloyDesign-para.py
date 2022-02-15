
import numpy as np
import pandas as pd
#from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from elements import *
from operator import itemgetter
import multiprocessing
from functools import partial

def cal_similarity(elements):
  sum=0
  N=(len(elements)-1)*len(elements)/2
  for i in range(0,len(elements)):
    for j in range(i+1,len(elements)):
      veci,vecj=np.asarray(elements[i]),np.asarray(elements[j])
      #print("dot: ",np.dot(veci,vecj),veci,vecj)
      sum += np.dot(veci,vecj)/np.linalg.norm(veci)/np.linalg.norm(vecj)
  return sum/N
def batch_cal_similarity3(elements,ELEMENTS):
  sim_all,sim_all_ordered=[],[]
  for i in range(0,len(elements)-2):
    for j in range(i+1,len(elements)-1):
      for k in range(j+1,len(elements)):
        arr=np.array([elements[i],elements[j],elements[k]])
        system=ELEMENTS[i]+ELEMENTS[j]+ELEMENTS[k]
        similarity=cal_similarity(arr)
        similarity=round(similarity,4)
        sim_all.append([system,similarity])
        sim_all_ordered.append([system,similarity])
  #sim_all_ordered=np.copy(sim_all)
  sim_all_ordered.sort(key=itemgetter(1),reverse=True)
  for i in range(0,len(sim_all)):
    sim_all[i].append(sim_all_ordered.index(sim_all[i]))
    #print("alloy, similarity: ",sim_all[i])
  return sim_all
def batch_cal_similarity4(elements,ELEMENTS):
  sim_all,sim_all_ordered=[],[]
  for j in range(0,len(elements)-3):
    for k in range(j+1,len(elements)-2):
      for l in range(k+1,len(elements)-1):
        for m in range(l+1,len(elements)):
          arr=np.array([elements[j],elements[k],elements[l],elements[m]])
          system=ELEMENTS[j]+ELEMENTS[k]+ELEMENTS[l]+ELEMENTS[m]
          similarity=cal_similarity(arr)
          similarity=round(similarity,4)
          sim_all.append([system,similarity])
          sim_all_ordered.append([system,similarity])
  sim_all_ordered.sort(key=itemgetter(1),reverse=True)
  for i in range(0,len(sim_all)):
    sim_all[i].append(int(sim_all_ordered.index(sim_all[i])))
    #print("alloy, similarity: ",sim_all[i])
    #print(sim_all[i][1])
  return sim_all
def batch_cal_similarity5(elements,ELEMENTS):
  sim_all,sim_all_ordered=[],[]
  for i in range(0,len(elements)-4):
    for j in range(i+1,len(elements)-3):
      for k in range(j+1,len(elements)-2):
        for l in range(k+1,len(elements)-1):
          for m in range(l+1,len(elements)):
            arr=np.array([elements[i],elements[j],elements[k],elements[l],elements[m]])
            system=ELEMENTS[i]+ELEMENTS[j]+ELEMENTS[k]+ELEMENTS[l]+ELEMENTS[m]
            similarity=cal_similarity(arr)
            similarity=round(similarity,4)
            sim_all.append([system,similarity])
            sim_all_ordered.append([system,similarity])
  sim_all_ordered.sort(key=itemgetter(1),reverse=True)
  for i in range(0,len(sim_all)):
    sim_all[i].append(int(sim_all_ordered.index(sim_all[i])))
    #print("alloy, similarity: ",sim_all[i])
    print(sim_all[i][1])
  return sim_all
def batch_cal_similarity6(elements,ELEMENTS):
  sim_all,sim_all_ordered=[],[]
  for i in range(0,len(elements)-5):
    for j in range(i+1,len(elements)-4):
      for k in range(j+1,len(elements)-3):
        for l in range(k+1,len(elements)-2):
          for m in range(l+1,len(elements)-1):
            for n in range(m+1,len(elements)):
              arr=np.array([elements[i],elements[j],elements[k],elements[l],elements[m],elements[n]])
              system=ELEMENTS[i]+ELEMENTS[j]+ELEMENTS[k]+ELEMENTS[l]+ELEMENTS[m]+ELEMENTS[n]
              similarity=cal_similarity(arr)
              #print("similarity: ",similarity)
              similarity=round(similarity,4)
              sim_all.append([system,similarity])
              sim_all_ordered.append([system,similarity])
  sim_all_ordered.sort(key=itemgetter(1),reverse=True)
  for i in range(0,len(sim_all)):
    sim_all[i].append(int(sim_all_ordered.index(sim_all[i])))
    #print("alloy, similarity: ",sim_all[i])
    #print(sim_all[i][1])
  #print("max,min: ",np.max(sim_all),np.min(sim_all))
  return sim_all
def batch_cal_similarity6p(offset,num_proc,elements,ELEMENTS):
  sim_all,sim_all_ordered=[],[]
  max_iter=len(elements)-5
  bin_size=int(max_iter/(num_proc-1))
  print("max_iter,bin_size: ",max_iter,bin_size)
  low,up=offset*bin_size,min(max_iter,(offset+1)*bin_size)
  print("low boundary, up boundary: ",low,up)
  for i in range(low,up):
  #for i in range(0,len(elements)-5):
    for j in range(i+1,len(elements)-4):
      for k in range(j+1,len(elements)-3):
        for l in range(k+1,len(elements)-2):
          for m in range(l+1,len(elements)-1):
            for n in range(m+1,len(elements)):
              arr=np.array([elements[i],elements[j],elements[k],elements[l],elements[m],elements[n]])
              system=ELEMENTS[i]+ELEMENTS[j]+ELEMENTS[k]+ELEMENTS[l]+ELEMENTS[m]+ELEMENTS[n]
              system1=ELEMENTS[i]+str(1)+ELEMENTS[j]+str(1)+ELEMENTS[k]+str(1)+ELEMENTS[l]+str(1)+ELEMENTS[m]+str(1)+ELEMENTS[n]+str(1)
              similarity=cal_similarity(arr)
              #print("similarity: ",similarity)
              similarity=round(similarity,4)
              sim_all.append([system1,system,similarity])
              sim_all_ordered.append([system,similarity])
  #sim_all_ordered.sort(key=itemgetter(1),reverse=True)
  #print("sim_all: ",sim_all)
  #for i in range(0,len(sim_all)):
  #  sim_all[i].append(int(sim_all_ordered.index(sim_all[i])))
    #print("alloy, similarity: ",sim_all[i])
    #print(sim_all[i][1])
  return sim_all

def batch_cal_similarity7(elements,ELEMENTS):
  sim_all,sim_all_ordered=[],[]
  for i in range(0,len(elements)-6):
    for j in range(i+1,len(elements)-5):
      for k in range(j+1,len(elements)-4):
        for l in range(k+1,len(elements)-3):
          for m in range(l+1,len(elements)-2):
            for n in range(m+1,len(elements)-1):
              for o in range(n+1,len(elements)):
                arr=np.array([elements[i],elements[j],elements[k],elements[l],elements[m],elements[n],elements[o]])
                system=ELEMENTS[i]+ELEMENTS[j]+ELEMENTS[k]+ELEMENTS[l]+ELEMENTS[m]+ELEMENTS[n]+ELEMENTS[o]
                similarity=cal_similarity(arr)
                similarity=round(similarity,4)
                sim_all.append([system1,system,similarity])
                sim_all_ordered.append([system,similarity])
  sim_all_ordered.sort(key=itemgetter(2),reverse=True)
  for i in range(0,len(sim_all)):
    sim_all[i].append(int(sim_all_ordered.index(sim_all[i])))
    #print("alloy, similarity: ",sim_all[i])
    #print(sim_all[i][1])
  return sim_all
def batch_cal_similarity7p(offset,num_proc,elements,ELEMENTS):
  sim_all,sim_all_ordered=[],[]
  max_iter=len(elements)-6
  if max_iter<num_proc+1:num_proc=max_iter-1
  bin_size=int(max_iter/(num_proc-1))
  print("max_iter,bin_size: ",max_iter,bin_size)
  low,up=offset*bin_size,min(max_iter,(offset+1)*bin_size)
  print("low boundary, up boundary: ",low,up)
  for i in range(low,up):
    for j in range(i+1,len(elements)-5):
      for k in range(j+1,len(elements)-4):
        for l in range(k+1,len(elements)-3):
          for m in range(l+1,len(elements)-2):
            for n in range(m+1,len(elements)-1):
              for o in range(n+1,len(elements)):
                arr=np.array([elements[i],elements[j],elements[k],elements[l],elements[m],elements[n],elements[o]])
                system=ELEMENTS[i]+ELEMENTS[j]+ELEMENTS[k]+ELEMENTS[l]+ELEMENTS[m]+ELEMENTS[n]+ELEMENTS[o]
                system1=ELEMENTS[i]+str(1)+ELEMENTS[j]+str(1)+ELEMENTS[k]+str(1)+ELEMENTS[l]+str(1)+ELEMENTS[m]+str(1)+ELEMENTS[n]+str(1)+ELEMENTS[o]+str(1)
                similarity=cal_similarity(arr)
                similarity=round(similarity,4)
                sim_all.append([system1,system,similarity])
                sim_all_ordered.append([system,similarity])
  return sim_all
def get_arr_similarity(num_component):
  num_proc=25 #5 #4
  pool = multiprocessing.Pool(num_proc)
  arr=[]
  ELEMENTS=element_short()
  #print(years)
  model="model_2018" #+str(i)
  data=pd.read_csv('elements_wv'+model+'_12-15-20.csv',index_col=None)
  #data=pd.read_csv('elements_wv'+model+'.csv',index_col=None)
  data=np.array(data)
  X=np.transpose(data)
  indices=[20,21,22,23,24,25,26,27,28,29,38,39,40,41,42,43,44,45,46,47,56,71,72,73,74,75,76,77,78,79] 
  #[range(20,30),range(38,48),56,range(71,80)]
  vects,ELEMS=[],[]
  for i in indices:
    vects.append(X[i]),ELEMS.append(ELEMENTS[i])
  #add five component
  if num_component==6:
    #arr_i=batch_cal_similarity6(vects,ELEMS) #(X[22:29],ELEMENTS[22:29])
    cal_sim_x=partial(batch_cal_similarity6p,num_proc=num_proc,elements=vects,ELEMENTS=ELEMS)
    arr_i=pool.map(cal_sim_x,range(num_proc))
    arr=[]
    for i in range(len(arr_i)):
      for j in range(len(arr_i[i])):
        arr.append(arr_i[i][j])
    #arr_i=batch_cal_similarity6p(vects,ELEMS)

  if num_component==7:
    #arr=batch_cal_similarity7(vects,ELEMS)
    cal_sim_x=partial(batch_cal_similarity7p,num_proc=num_proc,elements=vects,ELEMENTS=ELEMS)
    arr_i=pool.map(cal_sim_x,range(num_proc))
    arr=[]
    for i in range(len(arr_i)):
      for j in range(len(arr_i[i])):
        arr.append(arr_i[i][j])
  #arr.append(arr_i)
  ##add four component
  #arr_i=batch_cal_similarity4(vects,ELEMS)
  #arr.append(arr_i)
  ##add three component
  #arr_i=batch_cal_similarity3(vects,ELEMS)
  #arr.append(arr_i)
  print("num_proc: ",num_proc)
  print("Alloys of"+str(num_component)+"-components: ",len(arr))
  return arr
def count_S(array_1D,bin_size):
  num_bins=int(0.0/bin_size)
  counts,myBins=[],[]
  for i in range(0,num_bins):
    low,up=0.0+i*bin_size,0.0+(i+1)*bin_size
    stat=np.histogram(array_1D, bins=(low,up))
    count_i=stat[0]
    counts.append(count_i[0])
    myBins.append(low) #((low+up)/2.0)
    #print("mybin,count_i: ",low,count_i)
  return myBins,counts
if __name__=="__main__":
  import pandas as pd
  num_component=7 #6 #7
  sys_sim=get_arr_similarity(num_component)
  names=["sys1","sys","sim"]
  df=pd.DataFrame(sys_sim,columns=names)
  df.to_csv("sys_sim"+str(num_component)+".csv")
  #df=pd.read_csv("sys_sim"+str(num_component)+".csv")
  #similarity=df['sim']
  #print("df, sim: ",df,similarity)
  #bin_size=0.1
  #myBins,counts=count_S(similarity.to_numpy(),bin_size)
  #print("myBins,counts",myBins,counts)

#years=[2003,2004,2011,2014,2016,2018]
  #_,arr=get_arr_year(years)
  #new_arr=reorder_data_year(years,arr)
  #print("new_arr: ",new_arr)
  #plot(new_arr)

  #data=pd.read_csv('elements_wv.csv',index_col=None)
  #model="model_2003"
  #data=pd.read_csv('elements_wv'+model+'.csv',index_col=None)
  #data=np.array(data) #(header=False,index=False)
  #X=np.transpose(data)
  #X=data
  #print(X)
  #ELEMENTS=element_short()
  #print("total similarity: ",cal_similarity(X[23:28]))
  #print("total similarity: ",cal_similarity(X[23:28]))
  #batch_cal_similarity3(X[22:28],ELEMENTS[22:28])
  #batch_cal_similarity5(X[22:29],ELEMENTS[22:29])
  #vects=np.array([X[21],X[39],X[40],X[41],X[71],X[72],X[73]])
  #ELEMS=[ELEMENTS[21],ELEMENTS[39],ELEMENTS[40],ELEMENTS[41],ELEMENTS[71],ELEMENTS[72],ELEMENTS[73]]
  #print("Elements: ",ELEMS)
  #batch_cal_similarity5(vects,ELEMS)
