import MODULES.DATA.data_readin as dar
import MODULES.PLOTTING.plotting_general as pg
import MODULES.PLOTTING.retrieval_spectra as rs
import MODULES.STATISTICS.bayesian as bay

# GLOBALS
PLOT_SAVE_DIR = "PLOTS"
DATA_DIR = "DATA"
PLOT_TYPE = "png"


def main():

    observation = dar.ObservationDataEureka(
        filename=f"{DATA_DIR}/eureka_wasp39b_spectrum.dat"
    )

    wasp39b = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/eureka_wasp39b_noclouds.hdf5",
        name_id="Reference",
        colour="tab:blue"
    )

    nocloud = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/eureka_wasp39b.hdf5",
        name_id="No Cloud",
        colour="tab:orange"
    )

    noco2 = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/eureka_wasp39b_noCO2.hdf5",
        name_id="no CO2",
        colour="tab:green"
    )

    noch4 = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/eureka_wasp39b_noCH4.hdf5",
        name_id="no CH4",
        colour="tab:purple"
    )

    """
    sols = [wasp39b, nocloud, noch4, noco2]
    rs.plot_retrieval_spectrum(
        observation=observation,
        retrieval_spectra=sols2,
        savename="eureka_retrieval_spectra2.pdf"
    )
    """
    sols_talk = [
        [], [wasp39b], [wasp39b, nocloud],
        [wasp39b, nocloud, noch4, noco2]
    ]
    names_talk = ["empty", "reference", "nocloud", "nomols"]

    for i in range(len(sols_talk)):
        rs.plot_retrieval_spectrum(
            observation=observation,
            retrieval_spectra=sols_talk[i],
            savename=f"eureka_retrieval_{names_talk[i]}.{PLOT_TYPE}"
        )

    bay.bayes_analysis(sols_talk[-1])


if __name__ == "__main__":
    pg.rc_setup()
    main()
