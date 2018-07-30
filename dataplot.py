
# coding: utf-8

# In[ ]:


import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('elektra.dat',fsep=',')
BHID= files[:,1]
Time= files[:,2]
BHDistance= files[:,5]

ID=[89422247, 89422741, 89425759]

i1= np.where(BHID==89422247)
i2= np.where(BHID== 89422741)
i3= np.where(BHID== 89425759)
i4= np.where(BHID== 243770516)
i5= np.where(BHID== 243778457)
i6= np.where(BHID== 243771992)
i7= np.where(BHID== 307622464)
i8= np.where(BHID== 227839049)

#BHDistance.("]","")
#np.char.strip(BHDistance)
#Time= np.array(Time)

#BHDistance=np.array(BHDistance)


#print Time
#print BHDistance

plt.plot(Time[i1], BHDistance[i1],  label= "black hole 11")
plt.plot(Time[i2], BHDistance[i2], label= "black hole 10")
plt.plot(Time[i3], BHDistance[i3], label= "black hole 5")
plt.plot(Time[i3], BHDistance[i3], label= "black hole 16")
plt.plot(Time[i3], BHDistance[i3], label= "black hole 2a")
plt.plot(Time[i3], BHDistance[i3], label= "black hole 2b")
plt.plot(Time[i3], BHDistance[i3], label= "black hole 1")
plt.plot(Time[i3], BHDistance[i3], label= "black hole 3")

plt.ylabel("BH Distance 'Kpc'")
plt.xlabel("Time 'Gyr'")
plt.legend()
plt.show()


