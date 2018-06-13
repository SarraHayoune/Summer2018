
# coding: utf-8

# assignement: Find Black Hole 
# 

# In[20]:


import pynbody
import numpy as np
import pandas as pd
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)

s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')   
s.physical_units()
h = s.halos()
h5= h[5]

# initialize dataframe
columns = ['mass','haloid','BHpos','BHvel','redshift','time','bhiord','halodist','Mvir','Mstar','Mgas']
bhinfo = pd.DataFrame(columns=columns)

def findBH(h5):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    h5= snap.stars[BHfilter]
    return h5


data = [h5['pos'].in_units('kpc'),h5['r']]
info = pd.DataFrame(data,columns=columns)
bhinfo = bhinfo.append(info)
