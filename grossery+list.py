
# coding: utf-8

# In[21]:


import pandas as pd


f= open("list.txt","w")
data = ["banana","apple","potato", "tomato"]
f.write(str(data))
f= open("list.txt","r")

list = f.readline()
while list:
      items= list.split()
      dataitems= items()
      print (dataitems)
      list = f.readline()
f.close()
#print df

