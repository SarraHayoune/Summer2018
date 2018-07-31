
# coding: utf-8

# In[97]:


import matplotlib.pyplot as plt
import numpy as np
from Tkinter import *



#get_ipython().magic(u'matplotlib inline')

x = np.arange(5)
#y= [3,1,0,1,1]

plt.bar( x,color = 'darkblue', edgecolor = 'black', height=[4,2,0,1,1],width=.4)
plt.xticks(x+.25, [ 0,1,2,3,4])
plt.yticks(x+1)


plt.xlabel('distance from halo center (Kpc)',size= 18 )
plt.ylabel('BH Number',   size= 18)
main = Tk()

Label(main, 
		 text="Red Text in Times Font",
		 fg = "red",
		 font = "times 18 bold italic").pack()
#plt.legend()
plt.show('plot2.png')
