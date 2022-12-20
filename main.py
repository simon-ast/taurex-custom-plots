import numpy as np
import matplotlib.pyplot as plt
import h5py as h5
from MODULES.DATA import data_readin as dar
"""
GOAL:   Reproduce (somewhat) the plots provided by TauREx, but make them
        "nicer" (frame spacing etc.)
        
        The "Solutions" substructure stores numbered solutions. I wonder
        if this implies that several runs can be chained and evaluated
        together (maybe ask Ingo Waldmann about this)

PARTS:  Read in the data product. This will be a hdf5-file of the 
        retrieval results, with all necessary parameters
        
        Create Class/Dictionary storing all relevant information
        
        Create plotting routines, maybe they could read in a parameter
        file to determine what aspects to plot?


PSEUDCODE

"""

PLOT_SAVE_DIR = "PLOTS"
FILE = "DATA/retrieval.hdf5"
file_raw = h5.File(FILE)

output = file_raw["Output"]
sol0 = output["Solutions"]["solution0"]

test_ret = dar.TaurexSolution(identifier="Test", solution_group=sol0)

test1 = sol0["Spectra"]["Contributions"]["Absorption"]["binned_spectrum"][()]

spectrum = sol0["Spectra"]

binned_ret = spectrum["binned_spectrum"][()]
binned_std = spectrum["binned_std"][()]
binned_wl = spectrum["binned_wlgrid"][()]
binned_wlwidth = spectrum["binned_wlwidth"][()]

plt.plot(binned_wl, binned_ret)
plt.plot(binned_wl, test1)
plt.show()
exit()

plt.plot(binned_wl, binned_ret, marker="o")
plt.fill_between(binned_wl, y1=binned_ret-binned_std,
                 y2=binned_ret + binned_std, alpha=0.5)
plt.show()

exit()
# Binned spectrum
binned_spectrum = spectrum["binned_wlgrid"][()]
absorp = sol0["Spectra"]["Contributions"]["Absorption"]
co_xsec = absorp["CO"]["binned_spectrum"][()]
co2_xsec = absorp["CO2"]["binned_spectrum"][()]
h2o_xsec = absorp["H2O"]["binned_spectrum"][()]

plt.figure(1)
plt.plot(binned_spectrum, co_xsec)
plt.plot(binned_spectrum, co2_xsec)
plt.plot(binned_spectrum, h2o_xsec)

plt.savefig(f"{PLOT_SAVE_DIR}/binned_contrib.png", dpi=300)


# Native spectrum
native_spectrum = spectrum["native_wlgrid"][()]
absorp = sol0["Spectra"]["Contributions"]["Absorption"]
co_xsec = absorp["CO"]["native_spectrum"][()]
co2_xsec = absorp["CO2"]["native_spectrum"][()]
h2o_xsec = absorp["H2O"]["native_spectrum"][()]

plt.figure(2)
plt.plot(native_spectrum, co_xsec)
plt.plot(native_spectrum, co2_xsec)
plt.plot(native_spectrum, h2o_xsec)
plt.xlim(3, 5)

plt.savefig(f"{PLOT_SAVE_DIR}/native_contrib.png", dpi=300)


plt.show()

