
# coding: utf-8

# In[ ]:


Assignement: find black hole


# In[4]:


import pynbody
import matplotlib.pylab as plt

#im loading the snapshot                                                                   

s = pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

#save it by ctrl-x-s 'to save work'                                                        


# gonna start loading the halo'galaxies' now                                               

h = s.halos()

#halos we need to only look at # 5                                                         


pynbody.analysis.angmom.faceon(h[5])

#^^ its centering on the halo that i have picked which is 3 at the moment                  
#and giving it a shape of a disk almost like a dinner plate                                

s.physical_units()#^^ starts everything from the center reaching outwards almost like axis 

# find the BH in the snapshot
def findBH (s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = snap.stars[BHfilter]
    return BH

pynbody.analysis.halo.center(h[5],mode='hyb')

