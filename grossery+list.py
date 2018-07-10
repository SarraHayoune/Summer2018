
# coding: utf-8

# In[21]:


import pandas as pd


f= open("list.txt","w")
data = ["banana\n","apple\n","potato\n", "tomato\n"]
f.write(str(data))
f= open("list.txt","r")

print f.read()
f.close()
#print df

