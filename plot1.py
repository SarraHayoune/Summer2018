
# coding: utf-8

# In[ ]:


import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('bhfile.dat',fsep=',')
Time= files[:,2]
BHDistance= files[:,5]
print Time
print BHDistance

Time= np.array(Time)

BHDistance=np.array(BHDistance)



plt.plot(Time, BHDistance)

plt.xlabel('BH Distance')
plt.ylabel('Time')
plt.show()


