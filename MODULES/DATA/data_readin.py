"""
Reading and preparing result data for plotting

TODO: Solution read-in needs
    - Basic identifiers
    - Storage of Priors
    - Storage of binned and unbinned solution
    - Storage of contributions (mol. absorpt., rayleigh, etc)
        - Iterative filling (if present, then use etc.)
    - Storage of stats data (evidence etc)
"""
import h5py as h5


class TaurexSolution:
    """
    Wrapper class for all parameters of a specific TauREx retrieval
    solution. The solution is identified by a name ("identifier") and
    needs a hdf5-group from the TauREx retrieval file as an input
    ("solution group")
    """
    def __init__(self, identifier: str, solution_group):
        self.name_id = identifier

        # Data for the forward model spectrum is stored in the group
        # "Spectra"
        spectrum = solution_group["Spectra"]
        self.bin_solution = Spectrum("binned", spectrum)
        self.nat_solution = Spectrum("native", spectrum)

        # Statistical data is stored in the group "Statistics"
        stats = solution_group["Statistics"]
        self.logev = stats["Log-Evidence"][()]
        self.del_logev = stats["Log-Evidence-Error"][()]
        self.peakiness = stats["Peakiness"][()]

        # Individual contributions to the forward model are stored in
        # the group "Contributions" within "Spectra"
        # TODO: Sort out contribution loop for all parts
        contrib = spectrum["Contributions"]


class Spectrum:
    # TODO: Get identifier for the hdf5-group "spectrum"
    """
    Storage of binned or native spectra, opacity, wavelength and
    wave number grids.
    """
    def __init__(self, bin_type: str, spectrum_group):

        # SANITY CHECK: Only "binned" and "native" are valid options
        assert bin_type in ["binned", "native"]

        self.spectrum = spectrum_group[f"{bin_type}_spectrum"][()]
        self.std = spectrum_group[f"{bin_type}_std"][()]
        self.tau = spectrum_group[f"{bin_type}_tau"][()]
        self.wlgrid = spectrum_group[f"{bin_type}_wlgrid"][()]
        self.wlwidth = spectrum_group[f"{bin_type}_wlwidth"][()]
        self.wngrid = spectrum_group[f"{bin_type}_wngrid"][()]
        self.wnwidth = spectrum_group[f"{bin_type}_wnwidth"][()]
