import matplotlib as mpl
import matplotlib.pyplot as plt
import MODULES.DATA.data_readin as dar


def rc_setup():
    """Generalized plot attributes"""
    mpl.rcParams["xtick.direction"] = "in"
    mpl.rcParams["xtick.labelsize"] = "large"
    mpl.rcParams["xtick.major.width"] = 1.5
    mpl.rcParams["xtick.minor.width"] = 1.5
    mpl.rcParams["xtick.minor.visible"] = "True"
    mpl.rcParams["xtick.top"] = "True"

    mpl.rcParams["ytick.direction"] = "in"
    mpl.rcParams["ytick.labelsize"] = "large"
    mpl.rcParams["ytick.major.width"] = 1.5
    mpl.rcParams["ytick.minor.width"] = 1.5
    mpl.rcParams["ytick.minor.visible"] = "True"
    mpl.rcParams["ytick.right"] = "True"

    mpl.rcParams["axes.grid"] = "False"
    mpl.rcParams["axes.linewidth"] = 1.5
    mpl.rcParams["axes.labelsize"] = "large"

    mpl.rcParams["legend.frameon"] = "False"


def obs_spec(data: dar.ObservationData1366, ax: plt.Axes):
    """Plotting observational data into 'ax' object."""
    wavel = data.wl
    spec = data.tr_depth
    spec_up = data.tr_depth_errpos
    spec_lo = data.tr_depth_errneg

    ax.errorbar(
        x=wavel, y=spec, yerr=[spec_lo, spec_up],
        color="grey", marker="d", ms="5", mfc="tab:cyan", ls="",
        zorder=0, label="Observation"
    )
