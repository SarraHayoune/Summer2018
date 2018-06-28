# Assignement2" FIND ALL THE BLACK HOLES "

import pynbody 
import numpy as np
import matplotlib.pylab as plt

# loading the snapshot
s = pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')

# convert the units 
s.physical_units()

#  load any available halo
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

    
for i in halos:
    currenthalo = np.argsort(halos)
    print halos[currenthalo]
    # which halo are we on?  
    currenthalo= halos[i]
    print 'current halo: ', currenthalo
    halo=0
    if currenthalo != halo:  # need to center on new halo
       print currenthalo
       halo= currenthalo
     
       # put your galaxy that you care about in the center of the simulation
      
       pynbody.analysis.angmom.faceon(h[halo])
       with pynbody.analysis.halo.center(h[halo], mode='hyb'):
     
    # the position of black hole
            BHposition=BH['pos']
            print BHposition
      
   # x-values 
            BHx= BHposition[:,0]
    
   # y-values 
            BHy= BHposition[:,1]  
    
   # z-values 
            BHz= BHposition[:,2]
      
    #this is the distance formula
            distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
            print 'distance:', distance
   
      
       
        
