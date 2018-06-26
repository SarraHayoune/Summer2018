# Assignement2" FIND ALL THE BLACK HOLES "

import pynbody 
import numpy as np
import matplotlib.pylab as plt

# loading the snapshot
s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')  

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


for i in currenthalo:
    # which halo are we on?  
    currentBH = halos[i]
    print 'current halo: ',currentBH
        
    # put your galaxy that you care about in the center of the simulation
    halo= currentBH
    pynbody.analysis.angmom.faceon(h[halo])
    with pynbody.analysis.halo.center(h[halo], mode='hyb'):
     
    # the position of black hole
         #BHposition=BH['pos']
         #print BHposition
      
   # x-values 
         BHx= BHposition[i,0]
    
   # y-values 
         BHy= BHposition[i,1]  
    
   # z-values 
         BHz= BHposition[i,2]
      
    #this is the distance formula
         distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
         print distance
    
      
       
         
   
  
