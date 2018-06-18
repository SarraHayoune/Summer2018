   # assignement: Find Black Hole
import pynbody 
import numpy as np
import pandas as pd
  
  # loading the snapshot
s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

  # the halo that I need is h[5]
h = s.halos()
h5=h[5]

  # put your galaxy that you care about in the center of the simulation
pynbody.analysis.angmom.faceon(h5)

  # convert the units 
s.physical_units()
pynbody.analysis.halo.center(h5, mode='hyb')
print (h[5]['pos'][0])
print (h[5]['pos'][1])
print (h[5]['pos'][2])

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH
BH = findBH(s)

BH=BH['pos']
print BH

#this is the position of black hole
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

#the .5 is the square root , this is the distance formula
distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
print distance
