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


# TODO: Check type hinting for this (specifically "ax")
def retr_spec(data: dar.TaurexSolution, ax):
    """DOC!"""
    # Paramters for ease of reference
    wavel = data.bin_solution.wlgrid
    spec = data.bin_solution.spectrum
    stddev = data.bin_solution.std

    ax.plot(wavel, spec, label=data.name_id)

    # TODO: SHADED AREA WORKS, BUT STDDEV IS VERY SMALL
    ax.fill_between(
        x=wavel, y1=spec - stddev, y2=spec + stddev,
        alpha=0.5
    )


def obs_spec(data: dar.TaurexSolution, ax):
    """DOC!"""
    pass