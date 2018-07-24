
# Assignement4: make the time loop
import pynbody 
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
import readcol


files = readcol.readcol('bhfile.dat')
files = files[:,0]

# loading the snapshot
s =pynbody.load(file)
    #'/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

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

def getz(s):
    return s.properties['z']

def gettime(s):
    return pynbody.analysis.cosmology.age(s)
# initialize dataframe
#columns = ['BHpos','BHvel','redshift','time','bhiord','halodist']
#bhinfo = pd.DataFrame(columns=columns)

#f =  open("bhfile.dat", "w+") 
for file in files:
    for i in currenthalo:
    
        #which halo are we on?
        currenthalo = BHhalos[i]
        print 'current halo: ', currenthalo
        print i
    
        #put the galaxy you care about in the center of the simulation
        pynbody.analysis.angmom.faceon(h[currenthalo])

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
    
    #starmass = currenthalo.s['mass']
    #gasmass = currenthalo.g['mass']
    #virialmass = starmass+gasmass+currenthalo.d['mass']
        data = [currenthalo, BH['iord'][i], gettime(s),getz(s), BH['mass'][i], BH['r'][i]] 
        #f.write(str(data)+'\n')
    #f= open("bhfile.txt","w+")
    #for j in data:
        #f= open("bhfile.dat","w+")
       # info = pd.DataFrame(data,columns=columns)
       # bhinfo = bhinfo.append(info)
        #f.write(str(i))
    print data
         
f.close()

