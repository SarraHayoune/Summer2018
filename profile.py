import pynbody
import matplotlib.pylab as plt
import numpy as np

# load the snapshot and halo info
s = pynbody.load("/Jillian/cptmarvel/cptmarvel.cosmo25cmb.4096g5HbwK1BH.000672/cptmarvel.cosmo25cmb.4096g5HbwK1BH.000672")
h = s.halos()
s.physical_units()


# functions to find the BH and host halo
def findBH(snap):
    BHfilter = pynbody.filt.LowPass('tform',0.0)
    BH = snap.stars[BHfilter]
    return BH

def findBHhalos(snap):
    BH = findBH(snap)
    BHhalos = BH['amiga.grp']
    return BHhalos

# find the BH and host halo(s)
BH =findBH(s)
BHhalos = findBHhalos(s)
uniqueBHhalos = np.unique(BHhalos)
print uniqueBHhalos
nBH = len(BH) # how many BHs are there
nhalos = len(uniqueBHhalos) # how many halos hosting BHs are there
print nBH," black holes"
print nhalos," halos"

# loop through all halos and make density profiles
for halo in uniqueBHhalos:
    # center and align the halo
    pynbody.analysis.angmom.faceon(h[halo])
    # profile for stars
    pstar = pynbody.analysis.profile.Profile(h[halo].s,min=.01,max=30,ndim=3,type='log')
    # profile for gas
    pgas = pynbody.analysis.profile.Profile(h[halo].g,min=.01,max=30,ndim=3,type='log')
    # profile for all matter (star, gas, dark)
    pall = pynbody.analysis.profile.Profile(h[halo],min=.01,max=30,ndim=3,type='log')

    # set up the plot
    f, axs = plt.subplots(1,3,figsize=(14,6)) # 1,3 makes 1 row, 3 columns

    # plot the star profile
    axs[0].plot(pstar['rbins'],pstar['density'],'k')
    axs[0].semilogy()
    axs[0].semilogx()
    axs[0].set_xlabel('R [kpc]')
    axs[0].set_ylabel(r'$\rho_{\star}$ [M$_{\odot}$ kpc$^{-2}$')

    # plot the gas profile
    axs[1].plot(pgas['rbins'],pgas['density'],'k')
    axs[1].semilogy()
    axs[1].semilogx()
    axs[1].set_xlabel('R [kpc]')
    axs[1].set_ylabel(r'$\rho_{gas}$ [M$_{\odot}$ kpc$^{-2}$')
    axs[1].set_title("halo "+str(halo))

    # plot the total profile
    axs[2].plot(pall['rbins'],pall['density'],'k')
    axs[2].semilogy()
    axs[2].semilogx()
    axs[2].set_xlabel('R [kpc]')
    axs[2].set_ylabel(r'$\rho_{total}$ [M$_{\odot}$ kpc$^{-2}$')
    
    plt.savefig("profiles_halo"+str(halo)+".png")

    # write a file
    file = open("profiles_halo"+str(halo)+".dat","w")
    for i in range(len(pstar['rbins'])):
        row = str(pstar['rbins'][i])+' '+str(pstar['density'][i])+' '+str(pgas['rbins'][i])+' '+str(pgas['density'][i])+' '+str(pall['rbins'][i])+' '+str(pall['density'][i])
        file.write(row)
        file.write('\n')
    file.close()

