
# coding: utf-8

# assignement: Find Black Hole 
# 

# In[20]:


import pynbody
import numpy as np
import pandas as pd
import os
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)
import gc
get_ipython().magic(u'matplotlib inline')


# In[ ]:


s = pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')   
s.physical_units()
 pynbody.plot.image(h5.g, width=100, cmap='Blues');
h = s.halos()
h5= h[5]
pynbody.analysis.halo.center(h5,mode='hyb')
print(h[5]['pos'][0])

