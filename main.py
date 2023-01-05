import numpy as np

import MODULES.DATA.data_readin as dar
import MODULES.PLOTTING.plotting_general as pg
import MODULES.PLOTTING.retrieval_spectra as rs
import MODULES.STATISTICS.bayesian as bay

# GLOBALS
PLOT_SAVE_DIR = "PLOTS"
DATA_DIR = "DATA"


def main():

    observation = dar.ObservationData1366(
        filename=f"{DATA_DIR}/ERS1366_wasp39b_spectrum.txt"
    )

    nocloud = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/nocloud.hdf5",
        name_id="No Clouds",
        colour="tab:blue"
    )

    simcloud = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/simplecloud.hdf5",
        name_id="Fully opaque \n ($P_\\mathrm{top} \\approx 0.01$ mbar)",
        colour="tab:orange"
    )

    sols = [nocloud, simcloud]

    rs.plot_retrieval_spectrum(
        observation=observation,
        retrieval_spectra=sols,
        savename="acechem_retrieval_spectra.pdf"
    )

    bay.bayes_factor_display(sols)


if __name__ == "__main__":
    pg.rc_setup()
    main()
