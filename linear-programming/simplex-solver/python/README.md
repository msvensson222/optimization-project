# Simplex solver, implemented in Python

## Simplex
Currently trying to implement the Simplex algorithm in both Python and Rust, and benchmark the two.

**NOTE:** The current implementation, `SimplexSolver` found in `src/simplex.py`, does not work properly, and does not return the correct solution, thus the pytest fails.

## Getting started
Requirements:
  Python ^3.11

Navigate to the directory, and read the `README.md` file there:
```
make setup
```

To run tests, with the purpose of validating that the solver arrives at the optimal solution:
```
poetry run pytest -m unit
```

## Benchmarking
To benchmark your implementation, and get wall-clock times over many iterations, run:
```
poetry run pytest -m benchmark
```
