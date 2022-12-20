import matplotlib.pyplot as plt

import MODULES.DATA.data_readin as dar
import MODULES.PLOTTING.plotting_general as pg

# GLOBALS
PLOT_SAVE_DIR = "PLOTS"
DATA_DIR = "DATA"


def main():
    nocloud = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/nocloud.hdf5",
        name_id="No Clouds"
    )

    simcloud = dar.create_taurex_solution(
        filename=f"{DATA_DIR}/simplecloud.hdf5",
        name_id="Simple Clouds"
    )

    sols = [nocloud, simcloud]
    fig, ax = plt.subplots(figsize=(8, 4))

    plt.plot()

    for entry in sols:
        pg.retr_spec(entry, ax)

    plt.legend()
    plt.show()


if __name__ == "__main__":
    pg.rc_setup()
    main()
