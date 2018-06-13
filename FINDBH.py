
# coding: utf-8

# assignement: Find Black Hole 
# 

# In[20]:


import pynbody
import numpy as np
import pandas as pd

s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')   
h = s.halos()
pynbody.analysis.angmom.faceon(h[5])
s.physical_units()



def findBH(h5):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    h[5]= s.stars[BHfilter]
    return h[5]

p = pynbody.analysis.profile.Profile(h[5].s,min=.01,max=50)
