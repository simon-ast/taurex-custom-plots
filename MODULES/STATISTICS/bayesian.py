import numpy as np
import typing as tp


def bayes_factor_calculation(solutions: list) -> tp.Tuple:
    """
    Calculate the bayes factor for a list of solutions in the form of a
    2x2 array
    """
    log_ev_vec = np.array([[
        solution.logev for solution in solutions
    ]])

    bayes_factor = log_ev_vec - np.transpose(log_ev_vec)

    return log_ev_vec[0], bayes_factor


def bayes_factor_col(solutions: list) -> tp.Dict:
    """
    Collects solution IDs, log-evidence values and bayes factor as a 2D
    array
    """
    log_e, bf_arr = bayes_factor_calculation(solutions)
    sol_names = np.array([
        sol.name_id for sol in solutions
    ])

    return {
        "solution_names": sol_names,
        "log_evidence": log_e,
        "bayes_factor_array": bf_arr
    }


def bayes_analysis(solutions: list):
    """Print bayesian analysis to terminal (IDs, log(E) and log(B)"""
    bayes_dict = bayes_factor_col(solutions)
    num_sol = len(bayes_dict["solution_names"])

    print(f"\nIDs and log(E) for {num_sol} solution(s):\n")
    print_sol_names(bayes_dict["solution_names"])
    print_sol_evidence(bayes_dict["log_evidence"])

    print(f"\n\nValues for log(B0/B1):\n")
    print_bayes_factor(bayes_dict["bayes_factor_array"])
    print("\n")


def print_sol_names(sol_names: list) -> None:
    """Prints solution names in neat format"""
    separator = "\t"
    print(
        f'{separator.join(f"{name:<10}" for name in sol_names)}'
    )
    # Using the splat operator here look really neat, but it might not
    # be as useful
    # print(*sol_names, sep="\t")

    return None


def print_sol_evidence(log_ev: list) -> None:
    """Print log evidence values aligned with solution names"""
    separator = "\t"
    print(
        f'{separator.join(f"{le:<10.2f}" for le in log_ev)}'
    )

    return None


def print_bayes_factor(bayes_fac: np.ndarray) -> None:
    """Prints log Bayes Factor aligned with solution names"""
    for row in bayes_fac:
        entry_sep = "\t"
        print(
            f'{entry_sep.join(f"{bf:<10.2f}" for bf in row)}'
        )

    return None
