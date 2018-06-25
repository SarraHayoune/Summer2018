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
    
for halo in halos:
    # put your galaxy that you care about in the center of the simulation
    pynbody.analysis.angmom.faceon(h[halo])
   # convert the units 
    s.physical_units()
   # the halo that I need is h[5]
    h = s.halos()
    BH = findBH(s)
    halos = findBHhalos(s)
    sortedhaloinds = np.argsort(halos)
    print sortedhaloinds
    print halos[sortedhaloinds]
    halo = 0  # initialize what halo we are on
   
    for i in sortedhaloinds:
        # which halo are we on?  need to center 
        currenthalo = halos[i]
        print 'current halo: ',currenthalo
        if currenthalo != halo:  # need to center on new halo
            print "new halo calcs"
            halo = currenthalo
           
    with pynbody.analysis.halo.center(h[halo], mode='hyb'):
         print (h[halo]['pos'][0])
         print (h[halo]['pos'][1])
         print (h[halo]['pos'][2])
      
    
    #the position of black hole
    BHposition=BH['pos']
    print BHposition

   #putting the x-values into a column
    BHx= BHposition[:,0]
    print BHx

   #putting the y-values into a column
    BHy= BHposition[:,1]
    print BHy

   #putting the z-values into a column
    BHz= BHposition[:,2]
    print BHz

   #this is the distance formula
    distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
    print distance

