


import pynbody
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import readcol


files = readcol.readcol('testdata.txt')
Time= files[:,0]
BHDistance= files[:,3]

plt.plot(Time, BHDistance)
plt.ylabel('BH Distance')
plt.xlabel('Time')
plt.show()

