
# coding: utf-8

# In[21]:


import pandas as pd


f= open("list.txt","w")
data = ["banana","apple","potato", "tomato"]
f.write(str(data))
f= open("list.txt","r")

list = f.readline()
while list:
      data= list.split()
      f.write(data+'\n')
      print (data)
      list = f.readline()
f.close()
#print df

