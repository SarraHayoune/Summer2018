import pynbody
import matplotlib.pylab as plt
import numpy as np
import BH_FUNCTIONS as bhf
import readcol


#load the snapsho and set to physical units

s= pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')

#convert the units
s.physical_units()

#load the halos
h.s.halos()

#function to find the black hole
def findBH():
    BHfilter= pynbody.filt.LowPass('tform',0.0)
    BH= s.stars[BHfilter]
    return BH

BH= findBH(s)

# function to find the halos that the galaxy is in

def findBHhalos (s):
    BH= findBH(s)
    BHhalos = BH ['amiga.grp']
    return BHhalos
BHhalos = findBHhalos(s)

 # sorting halos
halolist= np.argsort(BHhalos)

for i in haloslist:
    currenthalo= BHhalos[i]
    print 'current halo: ', currenthalo
    print i


# center on halo and aligh the disc

    pynbody.analysis.halo.center(h[currenthalo], mode= 'hyb');
        
       

        #this is the position of black hole
    BHposition=BH['pos']

        #putting the x-values into a column
    BHx= BHposition[[i],0]
    print "x postion", BHx
   
        #putting the y-values into a column
    BHy= BHposition[[i],1]
    print "y position", BHy

         #putting the z-values into a column
    BHz= BHposition[[i],2]
    print "z position", BHz
    
    #plt.plot(BHx, BHy,'+') 
    #pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='halo'+str(currenthalo)+'.png')
    #plt.plot(BHx, BHy,'+')
                        
    plot_BH_pos(h[currenthalo].s, BH,'tform', w=20, save=True)

    



