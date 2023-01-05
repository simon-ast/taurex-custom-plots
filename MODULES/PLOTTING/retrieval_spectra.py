import matplotlib.pyplot as plt
import MODULES.PLOTTING.plotting_general as pg
import MODULES.DATA.data_readin as dar

# GLOBALS
PLOT_SAVE_DIR = "PLOTS"


def plot_retrieval_spectrum(observation, retrieval_spectra, savename):
    """Retrieval spectrum plot wrapper"""
    # Prepare plot
    fig, ax = setup_retr_spec()

    # Fill in observational data
    pg.obs_spec(observation, ax)

    # Fill in retrieval spectra
    for entry in retrieval_spectra:
        retr_spec(entry, ax)

    plt.legend(fontsize="large")
    plt.tight_layout()
    plt.savefig(f"{PLOT_SAVE_DIR}/{savename}")


def setup_retr_spec():
    """Setup for a one-panel retrieval spectrum plot"""
    fig, ax = plt.subplots(figsize=(8, 4))

    ax.set(
        xlabel="Wavelength [$\\mu$m]",
        ylabel="Transit depth [%]"
    )

    return fig, ax


def retr_spec(data: dar.TaurexSolution, ax: plt.Axes):
    """Plotting retrieved spectra into 'ax' object."""
    # Parameters for ease of reference
    wavel = data.bin_solution.wlgrid
    spec = data.bin_solution.spectrum * 100
    stddev = data.bin_solution.std * 100
    colour = data.colour

    ax.plot(wavel, spec, lw=2, label=data.name_id, c=colour)

    # TODO: SHADED AREA WORKS, BUT STDDEV IS VERY SMALL
    for i in [1, 2, 3]:
        ax.fill_between(
            x=wavel, y1=spec - i * stddev, y2=spec + i * stddev,
            alpha=0.4 - i * 0.1, color=colour
        )
