
# coding: utf-8

# In[21]:


import pandas as pd
f= open("list.txt","w")
data = [['banana',1],['apple',2],['fraise',3]]
df = pd.DataFrame(data,columns=['Name','Q'])
f.write(data)
f.close()
#print df

