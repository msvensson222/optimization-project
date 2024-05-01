import pytest

from src.linprog import lin_prog_solver
from src.problems import LP_PROBLEM


@pytest.mark.unit
def test_lin_prog_solver() -> None:
    """
    Test the lin_prog_solver function.

    This function tests the lin_prog_solver function by calling it and comparing the
    returned solution with the optimal solution of the LP problem. If the solution
    is invalid, an assertion error is raised.

    Returns:
        None
    """
    solution = lin_prog_solver()

    assert solution == LP_PROBLEM.optimal_solution, f"Invalid solution: {solution}"
