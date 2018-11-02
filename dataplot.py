
# coding: utf-8

# In[ ]:


import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('testdata.dat',fsep=',')
BHmass= files[:,2]
Time= files[:,0]
BHDistance= files[:,3]

#ID=[89422247, 89422741, 89425759]

#i1= np.where(BHID==89422247)
#i2= np.where(BHID== 89422741)
#i3= np.where(BHID== 89425759)
#i4= np.where(BHID== 243770516)
#i5= np.where(BHID== 243778457)
#i6= np.where(BHID== 243771992)
#i7= np.where(BHID== 307622464)
#i8= np.where(BHID== 227839049)

#BHDistance.("]","")
#np.char.strip(BHDistance)
#Time= np.array(Time)

#BHDistance=np.array(BHDistance)


#print Time
#print BHDistance

#plt.plot(Time[i1], BHDistance[i1],  label= "Captain Marvel")
#plt.plot(Time[i2], BHDistance[i2], label= "Captain Marvel")
#plt.plot(Time[i3], BHDistance[i3], label= "Captain Marvel")
#plt.plot(Time[i4], BHDistance[i4], label= "Storm")
#plt.plot(Time[i5], BHDistance[i5], label= "Strom")
#plt.plot(Time[i6], BHDistance[i6], label= "Storm")
#plt.plot(Time, BHDistance)
plt.ylabel("BH Mass 'Kpc'")
plt.xlabel("Time 'Gyr'")
plt.tick_params(axis="y", labelcolor="b")

#plt.twinx()
#plt.ylabel("BH Distance 'Kpc'")
#plt.tick_params(axis="y", labelcolor="r")

plt.legend()
plt.show()



