# assignement: Find Black Hole


import pynbody 
import numpy as np 
import pandas as pd 
pd.set_option('display.max_column', None)
pd.set_option('display.max_rows', None)

s =pynbody.load('/mnt/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096/cptmarvel.cosmo25cmb.4096g5HbwK1BH.004096') 
h = s.halos() 
pynbody.analysis.angmom.faceon(s) 
p = pynbody.analysis.profile.Profile(h[5].s,min=.01,max=50,ndim=3) 
pynbody.analysis.halo.center(h[5],mode='hyb') 
s.physical_units() 

def findBH(s):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = s.stars[BHfilter]
    return B

grpid=1
w=80;

pynbody.analysis.halo.center(h[grpid],mode='ssc');
pynbody.analysis.angmom.faceon(h[grpid], cen=(0,0,0))

BH=s.star[pynbody.filt.BandPass('tform','-15 Gyr','0 Gyr')]
BH_pos=BH['pos']
nBH=len(BH['iord']);

h[grpid].s['tform'].convert_units('Gyr');

pynbody.plot.image(h[grpid].s,qty="tform",cmap="Greys", width=w, log=False);
plt.plot(np.array((BH[np.where(BH['amiga.grp']==grpid)]['pos'])).T[0],np.array((BH[np.where(BH['amiga.grp']==grpid)]['pos'])).T[1],'r+')
plt.xlim(-w/2,w/2)
plt.ylim(-w/2,w/2);
