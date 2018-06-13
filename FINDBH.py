
# coding: utf-8

# assignement: Find Black Hole 
# 

# In[20]:


import pynbody
import numpy as np
import pandas as pd

s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')   
s.physical_units()
pynbody.analysis.angmom.faceon(h[5])
h[5]= s.halos()

def findBH(h5):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    h5= s.stars[BHfilter]
    return h[5]


