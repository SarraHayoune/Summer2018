import pynbody
import matplotlib.pylab as plt
import numpy as np
import BH_functions as BHF

# load the snapshot and set to physical units

#s= pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')
s= pynbody.load('/Jillian/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')

# convert the units
s.physical_units()

 # load the halos
h = s.halos()

 # function to find black hole
def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

BH = findBH(s)

# function to find the halos that the galaxy is in
def findBHhalos (s):
    BH = findBH(s)
    BHhalos = BH ['amiga.grp']
    return BHhalos

#pynbody.analysis.halo.center(h[2], mode= 'hyb');
pynbody.analysis.angmom.faceon(h[2])
#BHF.analysis(h[2], 'faceon')
 #this is the position of black hole
BHposition=BH['pos']

        #putting the x-values into a column
BHx1= BHposition[[1],0]
BHx2= BHposition[[2],0]
    #print "x postion", BHx
   
        #putting the y-values into a column
BHy1= BHposition[[1],1]
BHy2= BHposition[[2],1]
    #print "y position", BHy
         #putting the z-values into a column
BHz1= BHposition[[1],2]
BHz2= BHposition[[2],2]
    #print "z position", BHz
   
    #plt.plot(BHx, BHy,'+') 
  
BHF.render(s,width= '25 kpc',plot= True, ret_im= True, filename='stormbhpictures.png')

plt.plot(BHx1, BHy1,'+')
plt.plot(BHx2, BHy2,'+')
#BHF.render(s,width= '10 kpc', filename='stormbhpicture.png')
#plot.BH_pos(h[2].s, BH, 'tform', w=20, save= True)


plt.savefig('stormpicturefaceon.png')

   
