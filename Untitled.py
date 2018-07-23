
# coding: utf-8

# In[10]:


import pynbody
import numpy as np
import pandas as pd
import os
import readcol


files = readcol.readcol('testdata.txt')
Time= files[:,0]
BHDistance= files[:,3]
plt.plot(time, BHdistance)
plt.ylabel('BH Distance')
plt.xlabel('Time')
plt.show()

