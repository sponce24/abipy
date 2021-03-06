# This examples shows how to plot the GW self-energy
# and the spectral function of Al at the gamma point (first band)
# See lesson tgw2_4
from abipy import *

sigma_file = SIGRES_File(get_reference_file("tgw2_4o_SIGRES.nc"))

sigmaw = sigma_file.get_sigmaw(spin=0, kpoint=(0,0,0), band=0)

sigmaw.plot()
