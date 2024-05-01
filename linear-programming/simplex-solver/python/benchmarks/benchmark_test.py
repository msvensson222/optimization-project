import time
from typing import Any, Callable

import pytest

from src.linprog import lin_prog_solver
from src.problems import LP_PROBLEM


@pytest.mark.benchmark(
    group="linprog", min_rounds=10, timer=time.time, disable_gc=True, warmup=False
)
def test_lin_prog_benchmark(benchmark: Callable[..., Any]) -> None:
    """
    Test function for benchmarking the lin_prog_solver.

    Args:
        benchmark: The benchmark fixture provided by the pytest-benchmark library.

    Returns:
        None
    """
    solution = benchmark(lin_prog_solver)

    assert solution == LP_PROBLEM.optimal_solution, f"Invalid solution: {solution}"
