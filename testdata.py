


import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('testdata.txt')
Time= files[:,0]
BHmass = files [:,2]
BHDistance= files[:,3]

#plt.plot(Time, BHDistance)
#plt.ylabel('BH Distance')
#plt.xlabel('Time')

plt.plot(Time, BHmass)
plt.ylabel("BH Mass 'Kpc'")
plt.xlabel("Time 'Gyr'")
plt.tick_params(axis="y", labelcolor="b")

plt.plot(Time, BHDistance)
plt.twinx()
plt.ylabel("BH Distance 'Kpc'")
plt.tick_params(axis="y", labelcolor="r")

plt.show()

