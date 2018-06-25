# Assignement2" FIND ALL THE BLACK HOLES "

import pynbody 
import numpy as np
import matplotlib.pylab as plt

 # loading the snapshot
s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')
 
   # convert the units 
s.physical_units()
# the halo that I need is h[5]
h = s.halos()
 # function to find black hole
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)
print BH

def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos
halos = findBHhalos(s)
print halos 
    
for halo in h:
    print 'current halo:', halo
  
    # put your galaxy that you care about in the center of the simulation

     pynbody.analysis.angmom.faceon(h[halo])
   # convert the units 
       s.physical_units()
   # the halo that I need is h[5]
     halo = 0  # initialize what halo we are on
   
     with pynbody.analysis.halo.center(h[halo], mode='hyb'):
             print (h[halo]['pos'][0])
             print (h[halo]['pos'][1])
             print (h[halo]['pos'][2])
    #this is the distance formula
     distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
     print distance
   
      
   
  
