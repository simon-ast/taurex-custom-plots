import numpy as np

import MODULES.DATA.data_readin as dar
import MODULES.PLOTTING.plotting_general as pg
import MODULES.PLOTTING.retrieval_spectra as rs
import MODULES.STATISTICS.bayesian as bay

# GLOBALS
PLOT_SAVE_DIR = "PLOTS"
DATA_DIR = "DATA"


def main():

    observation = dar.ObservationDataEureka(
        filename=f"{DATA_DIR}/eureka_wasp39b_spectrum.dat"
    )

    nocloud = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/eureka_wasp39b.hdf5",
        name_id="No Clouds",
        colour="tab:blue"
    )

    wasp39b = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/eureka_wasp39b_noclouds.hdf5",
        name_id="Fully opaque",
        colour="tab:orange"
    )

    noco2 = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/eureka_wasp39b_noCO2.hdf5",
        name_id="no CO2",
        colour="tab:green"
    )

    sols = [noco2, nocloud, wasp39b]

    rs.plot_retrieval_spectrum(
        observation=observation,
        retrieval_spectra=sols,
        savename="eureka_retrieval_spectra.pdf"
    )

    bay.bayes_factor_display(sols)


if __name__ == "__main__":
    pg.rc_setup()
    main()
