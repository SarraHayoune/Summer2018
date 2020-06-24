
import pynbody
import matplotlib.pylab as plt
import numpy as np
import BH_FUNCTIONS as bhf
import readcol
# load the snapshot and set to physical units

#s= pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

files= readcol.readcol('/mnt/storm/files.list')
files = files[:,0]

 # function to find black hole
def findBH(S):
   # BHfilter =np.where(s.stars['iord']==89425759)
    BHfilter = np.where(s.stars['iord']== 243778457)
    
    #pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return BH

# function to find the halos that the galaxy is in
def findBHhalos (s):
    BH = findBH(s)
    BHhalos = BH ['amiga.grp']
    return BHhalos




 #sorting the halos, indexes/indecis are like an exact address



def gettime(s):
    return pynbody.analysis.cosmology.age(s)


for i in range(32,40):
    file  = files[i]
    s= pynbody.load('/mnt/storm/'+file)
    # convert the units
    s.physical_units()

    # load the halos
    h = s.halos()
    BH = findBH(s)
    BHhalos = findBHhalos(s)
    
   # halolist = np.argsort(BHhalos)
   # print BHhalos[currenthalo]
    
        #which halo are we on?
    currenthalo = BHhalos
    print 'current halo: ', currenthalo
    #print i
    

 # center on the largest halo and aligh the disk
      
    pynbody.analysis.halo.center(h[BHhalos], mode= 'hyb');
   

        #this is the position of black hole
    BHposition=BH['pos']
    BHposition= BHposition[0]
    print BHposition.shape
    print BHposition
        #putting the x-values into a column
    BHx= BHposition[0]
    print "x postion", BHx
   
        #putting the y-values into a column
    BHy= BHposition[1]
    print "y position", BHy

         #putting the z-values into a column
    BHz= BHposition[2]
    print "z position", BHz
    
    # create an image using  the default bands (i, v, u)
    #plt.plot(BHx, BHy,'+') 
    pynbody.plot.stars.render(s,width='5 kpc',plot=True,ret_im=True,filename='halo'+str(currenthalo)+'.png') 
          
    bhf.render(s,width = '5 kpc')
    plt.plot(BHx, BHy,'+')
    plt.savefig('/mnt/storm/'+file+'.BHpictures.png')
   
   

   
