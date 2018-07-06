
# coding: utf-8

# In[ ]:


# Assignement2" FIND ALL THE BLACK HOLES "

import pynbody 
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import os
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)
import readcol
import gc


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

#function to find the halos that the galaxy is in
def findBHhalos(s):
    BH = findBH(s)
    BHhalos = BH['amiga.grp']
    return BHhalos

#using the function the halos
BHhalos = findBHhalos(s)
print BHhalos

#sorting the halos, indexes/indecis are like an exact address
currenthalo = np.argsort(BHhalos)
print BHhalos[currenthalo]

f = open("bhfile.dat","w")
# initialize dataframe
columns = ['mass','haloid','BHpos','BHvel','redshift','time','bhiord','halodist','Mvir','Mstar','Mgas']
bhinfo = pd.DataFrame(columns=columns)
for i in currenthalo:

    #which halo are we on?
    currenthalo = BHhalos[i]
    print 'current halo: ', currenthalo
    print i
    
    #put the galaxy you care about in the center of the simulation
    pynbody.analysis.angmom.faceon(h[currenthalo])
    #with pynbody.analysis.halo.center(h[currenthalo], mode='hyb'):

#for halo in BHhalos:
#    halo/galaxy we need to look at is no. 2
#    pynbody.analysis.angmom.faceon(h[halo])
#    prints the black hole
#    print BH

    #this is the position of black hole
    BHposition=BH['pos']

    #printing the position of black hole
    #print BHposition

    #putting the x-values into a column
    BHx= BHposition[[i],0]
    print "x postion", BHx

    #putting the y-values into a column
    BHy= BHposition[[i],1]
    print "y position", BHy

    #putting the z-values into a column
    BHz= BHposition[[i],2]
    print "z position", BHz

    #the .5 is the square root , this is the distance formula
    distance =((BHx**2)+(BHy**2)+(BHz**2))**(.5)
    #print 'this is the distance :'
    print "this is the distance :", distance

    data = [[BH['mass'][i],BHhalos[i],BH['pos'][i].in_units('kpc'),BH['vel'][i],getz(s),gettime(s),BH['iord'][i],BH['r'][i],virialmass,starmass,gasmass]]
    info = pd.DataFrame(data,columns=columns)
    bhinfo = bhinfo.append(info)
    close().
