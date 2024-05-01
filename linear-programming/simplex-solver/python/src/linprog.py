from scipy.optimize import linprog

from src.problems import LP_PROBLEM, Solution


def lin_prog_solver() -> Solution:
    """
    Solves a linear programming problem using the linprog interfact, and the highs solver.

    Returns:
        An object containing the optimal value and solution.
    """
    result = linprog(
        LP_PROBLEM.c, A_ub=LP_PROBLEM.A, b_ub=LP_PROBLEM.b, bounds=LP_PROBLEM.bounds, method="highs"
    )
    return Solution(optimal_value=result.fun, optimal_solution=result.x)
