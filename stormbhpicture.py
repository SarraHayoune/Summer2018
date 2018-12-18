import pynbody
import matplotlib.pylab as plt
import numpy as np
import BH_FUNCTIONS.py as BHF

# load the snapshot and set to physical units

#s= pynbody.load('/mnt/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')
s= pynbody.load('/jillian/storm/storm.cosmo25cmb.4096g5HbwK1BH.004096/storm.cosmo25cmb.4096g5HbwK1BH.004096')

# convert the units
s.physical_units()

 # load the halos
h = s.halos()

 # function to find black hole
def findBH(S):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

BH = findBH(s)

# function to find the halos that the galaxy is in
def findBHhalos (s):
    BH = findBH(s)
    BHhalos = BH ['amiga.grp']
    return BHhalos


BHhalos = findBHhalos(s)

 #sorting the halos, indexes/indecis are like an exact address
halolist = np.argsort(BHhalos)
#print BHhalos[currenthalo]



#for i in halolist:
    
        #which halo are we on?
currenthalo = BHhalos[h[2]]
print 'current halo: ', currenthalo
    #print i
    

 # center on the largest halo and aligh the disk
      
    #pynbody.analysis.halo.center(h[2], mode= 'hyb');
pynbody.analysis.angmom.faceon(h[2])
        
       

        #this is the position of black hole
 BHposition=BH['pos']

        #putting the x-values into a column
 BHx1= BHposition[[0],0]
 BHx2= BHposition[[1],0]
    #print "x postion", BHx
   
        #putting the y-values into a column
 BHy1= BHposition[[0],1]
 BHy2= BHposition[[1],1]
    #print "y position", BHy

         #putting the z-values into a column
 BHz1= BHposition[[0],2]
 BHz2= BHposition[[1],2]
    #print "z position", BHz
   
    #plt.plot(BHx, BHy,'+') 
   # create an image using  the default bands (i, v, u)
  #pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='halo'+str(h2)+'.png')
  BHF.render(s,width= '5 kpc', filename='stormbhpicture.png')
  plt.plot(BHx1, BHy1,'+')
  plt.plot(BHx2, BHy2,'+')
  plt.savefig('stormpicture.png')
   
    # center on the largest halo and aligh the disk
 
#pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='haloFaceon.png')
# center on the largest halo and aligh the disk
#pynbody.analysis.angmom.sideon(h[5])
# create an image using  the default bands (i, v, u)
#pynbody.plot.stars.render(s,width= '10 kpc',plot=True,ret_im=True,filename='halo11edgeon.png')
                        
 #plot_BH_pos(h[2].s, BH,'tform', w=20, save=True)
 
