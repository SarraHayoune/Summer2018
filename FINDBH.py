# assignement: Find Black Hole

import pynbody 
import numpy as np 
import pandas as pd 
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)

s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096') 
h = s.halos() 
pynbody.analysis.angmom.faceon(h[5]) 
p = pynbody.analysis.profile.Profile(h[5].s,min=.01,max=50) 
pynbody.analysis.halo.center(h[5],mode='hyb') 
s.physical_units() 

def findBH(h5): 
   BHfilter = pynbody.filt.LowPass('tform',0.0) 
   BH = s.stars[BHfilter] 
   return h[5] 
    
columns = ['BHpos','BHvel','halodist']
bhinfo = pd.DataFrame(columns=columns)

# find the BHs
    BH = findBH(s)
    BHhalos = findBHhalos(s)
    nBH = len(BHhalos)
    
    data = [[BH['mass'],BHhalos,BH['pos'].in_units('kpc'),BH['vel'],BH['r'][i]]]
            info = pd.DataFrame(data,columns=columns)
            bhinfo = bhinfo.append(info)

    del(BH)
    del(h)
    del(s)
