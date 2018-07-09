
# coding: utf-8

# In[21]:


import pandas as pd


f= open("list.txt","w+")
data = ["banana","apple","potato", "tomato"]
f.write("data")
#f= open("list.txt","r")
for data in f:
    print (data)
f.close()
#print df

