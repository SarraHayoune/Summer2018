
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
def findBH(h[5]):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = snap.stars[BHfilter]
    return BH

def findBHhalos(h[5]):
    BH = findBH(h[5])
    BHhalos = BH['amiga.grp']
    return BHhalos
 for i in sortedhaloinds:
        # which halo are we on?  need to center 
        currenthalo = BHhalos[i]
        print 'current halo: ',currenthalo
        if currenthalo != halo:  # need to center on new halo
            print "new halo calcs"
            halo = currenthalo
            pynbody.analysis.halo.center(h[currenthalo],mode='ssc')

data = [BHhalos[i],BH['pos'][i].in_units('kpc'),getz(s),gettime(s),BH['r'][i]]
            info = pd.DataFrame(data,columns=columns)
            bhinfo = bhinfo.append(info)
