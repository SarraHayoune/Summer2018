
# coding: utf-8

# In[21]:


import pandas as pd


f= open("list.txt","a+")
data = ["banana\n","apple\n","potato\n", "tomato\n"]
f.write(data)
f= open("list.txt","r")

print f.read()
f.close()
#print df

