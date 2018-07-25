
# coding: utf-8

# In[ ]:


import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('bhfile.dat',fsep=',')
BHID= files[:,1]
Time= files[:,2]
BHDistance= files[:,5]

ID=[89422247, 89422741, 89425759]
i1= np.where(ID== 89422247)
i2= np.where(ID== 89422741)
i3= np.where(ID== 89425759)


#BHDistance.("]","")
#np.char.strip(BHDistance)
Time= np.array(Time)

BHDistance=np.array(BHDistance)


print Time
print BHDistance

plt.plot(Time[i1,i2,i3], BHDistance[i1,i2,i3])
#plt.plot(Time[i2], BHDistance[i2])
#plt.plot(Time[i3], BHDistance[i3])

plt.ylabel('BH Distance')
plt.xlabel('Time')
plt.show()


