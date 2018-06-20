
# coding: utf-8

# Assignement2" FIND ALL THE BLACK HOLES "

# In[ ]:


import pynbody 
import matplotlib.pylab as plt
plt.switch_backend("agg") 

   # loading the snapshot
s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

   # convert the units 
s.physical_units()

  # the halo that I need is h[5]
h = s.halos()

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH[0,1,2]
BH = findBH(s)
print BH
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

