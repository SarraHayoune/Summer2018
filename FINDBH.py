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

f, axs = plt.subplots(figsize=(14,6))
axs.plot(p['rbins'],p['density'], 'k')
axs.semilogy()
axs.set_xlabel('R [kpc]''Density PLOT OF H05')
axs.set_ylabel(r'$\rho_{DM}$ [M$_{\odot}$ kpc$^{-3}$]')
#^^^ lines are writing the graph up
plt.savefig("ThePlotFor11.png")
