
# coding: utf-8

# In[21]:


import pandas as pd


f= open("list.txt","w")
data = [1,2,3,4,"banana","apple","potato", "tomato"]
f.write(str(data))
f= open("list.txt","r")

f= open("list.txt","w")
for i in data:
    f.write(str(i)+'\n')
    print i



#list = f.readline()
#while list:
      #data= list.split()
      #f.write(data+'\n')
      #print (data)
      #list = f.readline()
f.close()
#print df

