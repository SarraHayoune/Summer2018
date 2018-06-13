
# coding: utf-8

# assignement: Find Black Hole 
# 

# In[20]:


import pynbody
import numpy as np
import pandas as pd

s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')   
s.physical_units()
h = s.halos()
h5= h[5]
def findBH(h5):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    h5= snap.stars[BHfilter]
    return h5


data = [h5['pos'][i].in_units('kpc'),getz(s),gettime(s),h5['r'][i]]
info = pd.DataFrame(data,columns=columns)
bhinfo = bhinfo.append(info)
