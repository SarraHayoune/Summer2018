
import pynbody
import matplotlib.pylab as plt
import numpy as np

# load the snapshot and set to physical units

s= pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096')

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
def plot_BH_pos(h, BH, attribute, cmap='Greys', w=100, lc='best',save=False, filename='plots/dg_adjTime/h%s_t%s_w%s.png'):
    '''plots position of black holes. Send halo array(h[grpid]), black hole array(BH),attribute 
    Optional: width/preferred scope(w) (default=100), colormap(default='Greys'), save(default=False)'''
    
    halo_id=int(np.unique(h['amiga.grp']))
    time=h.properties['time'].in_units('Gyr')
    
    pynbody.plot.image(h,qty=attribute,cmap=cmap, width=w, log=False)
    for i in np.where(BH['amiga.grp']==halo_id):
        plt.plot(np.array(BH[i]['pos']).T[0],np.array(BH[i]['pos']).T[1],'r+', label=BH[i]['iord'])
    plt.xlim(-w/2,w/2)
    plt.ylim(-w/2,w/2)
    plt.title('Halo %s at %s Gyr'%(halo_id, round(time, 1)))
    plt.legend(fancybox=True, loc='lc')
    plt.tight_layout()

    if save==True:
        plt.savefig(filename%(halo_id, round(time, 1), w),bbox_inches='tight', dpi=200)

        


for i in halolist:
    
        #which halo are we on?
    currenthalo = BHhalos[i]
    print 'current halo: ', currenthalo
    print i
    

 # center on the largest halo and aligh the disk
      
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
    # create an image using  the default bands (i, v, u)
    #plt.plot(BHx, BHy,'+') 
    #pynbody.plot.stars.render(s,width= '5 kpc',plot=True,ret_im=True,filename='halo'+str(currenthalo)+'.png')
    #plt.plot(BHx, BHy,'+')
                        
    plot_BH_pos(h[currenthalo].s, BH,'tform', w=20, save=True)
