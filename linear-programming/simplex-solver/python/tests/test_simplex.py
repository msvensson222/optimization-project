import pytest

from src.problems import LP_PROBLEM
from src.simplex import simplex


@pytest.mark.unit
def test_simplex_solver() -> None:
    """
    Test the simplex solver function.

    This function calls the simplex solver and asserts that the obtained solution
    matches the optimal solution of the LP problem.

    Raises:
        AssertionError: If the obtained solution is invalid.

    Returns:
        None
    """
    solution = simplex()

    assert solution == LP_PROBLEM.optimal_solution, f"Invalid solution: {solution}"
