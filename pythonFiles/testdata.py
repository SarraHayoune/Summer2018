

#import pynbody
import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('storm.dat',fsep=',')

Time= files[:,2]
BHdistance= files[:, 5]
#print BHdistance 
VirialMass= files[:, 8]
BHID= files [:, 1]
#i1= [ 89422247]
      #, 89422741, 89425759]

#i1= np.where(BHID==89422247)# 10
#print i1[0]
#i2= np.where(BHID== 89422741)#11
#i3= np.where(BHID== 89425759)#5
#i4= np.where(BHID== 243770516)
#i5= np.where(BHID== 243778457)
i6= np.where(BHID== 243771992)
#i7= np.where(BHID== 307622464)
#i8= np.where(BHID== 227839049)

#BHDistance.("]","")
#np.char.strip(BHDistance)
#Time= np.array(Time)

#BHDistance=np.array(BHDistance)


#print Time
#print BHDistance
plt.xlabel("Time 'Gyr'")
plt.ylabel("BH Distance ")
plt.ylim(0, 1)
#plt.plot(Time[i1],BHdistance[i1],color= "b",  label= "Captain Marvel BH-10")
plt.plot(Time[i6],BHdistance [i6],color= "b", label= "Storm BH-2b")
#plt.plot(Time[i3], BHdistance[i3],color= "b", label= "Captain Marvel BH-5")
plt.tick_params(axis="y", labelcolor="b")


plt.twinx()
plt.ylabel("VirialMass")
#plt.plot(Time[i1], VirialMass[i1], color= "r",  label= "Captain Marvel BH-10")
plt.plot(Time[i6], VirialMass[i6], color= "r",  label= "Storm  BH-2b")
#plt.plot(Time[i3], VirialMass[i3], color= "r", label= "Captain Marvel BH-5")
plt.yscale('log')
#plt.xlabel("Time 'Gyr'")

plt.tick_params(axis="y", labelcolor="r")

#plt.plot(Time[i4], BHDistance[i4], label= "Storm")
#plt.plot(Time[i5], BHDistance[i5], label= "Strom")
#plt.plot(Time[i6], BHDistance[i6], label= "Storm")

#plt.plot(Time, BHmass)

#plt.plot(Time, VirialMass)


plt.legend()
plt.show()



