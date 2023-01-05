import numpy as np


def bayes_factor_calculation(solutions: list):
    """
    Calculate the bayes factor for a list of solutions in the form of a
    2x2 array
    """
    log_ev_vec = np.array([[
        solution.logev for solution in solutions
    ]])

    bayes_factor = log_ev_vec - np.transpose(log_ev_vec)

    return log_ev_vec[0], bayes_factor


def bayes_factor_display(solutions: list):
    """DOC!"""
    log_e, bf_arr = bayes_factor_calculation(solutions)
    sol_names = np.array([
        sol.name_id for sol in solutions
    ])

    print(sol_names)
    print(log_e)
    print(bf_arr)
