import numpy as np

from src.problems import LP_PROBLEM, Solution


class SimplexSolver:
    """
    A class that implements the Simplex algorithm for solving linear programming problems.

    Args:
        c : Cost function coefficients.
        A : Constraint coefficients.
        b : Right-hand side of constraints.

    Attributes:
        c: Cost function coefficients.
        A: Constraint coefficients.
        b: Right-hand side of constraints.
        n: Number of variables.
        m: Number of constraints.

    Methods:
        solve(): Solves the linear programming problem and returns the optimal solution.

    """

    def __init__(self, c: list[float], A: list[list[float]], b: list[float]):
        self.c = np.array(c, dtype=float)  # Cost function coefficients
        self.A = np.array(A, dtype=float)  # Constraint coefficients
        self.b = np.array(b, dtype=float)  # Right-hand side of constraints
        self.n = len(c)  # Number of variables
        self.m = len(b)  # Number of constraints

    def solve(self) -> Solution:
        """
        Solves the linear programming problem and returns the optimal solution.

        Returns:
            An object containing the optimal value and solution.

        Raises:
            Exception: If the LP problem is unbounded or infeasible.
        """
        # Add slack variables to A and extend cost function with zeros for these variables
        tableau = np.hstack((self.A, np.eye(self.m), self.b.reshape(-1, 1)))
        c_extended = np.concatenate(
            (self.c, np.zeros(self.m))
        )  # Full cost row including zeros for slacks
        cb_indices = np.array(
            range(self.n, self.n + self.m)
        )  # Indices of basic variables, initially slacks

        # Initialize the objective row in the tableau
        obj_row = np.zeros(self.n + self.m + 1)  # Full objective row
        obj_row[: self.n] = self.c  # Set initial costs (excluding slacks)

        # Subtract the linear combination of rows corresponding to basic variables from the objective row
        for i in range(self.m):
            obj_row -= c_extended[cb_indices[i]] * tableau[i]

        while True:
            # Calculate reduced costs for all variables
            reduced_costs = obj_row[:-1] - np.dot(tableau.T[:-1], obj_row[cb_indices])

            # If all reduced costs are non-negative, current solution is optimal
            if np.all(reduced_costs >= 0):
                break

            # Select entering variable (most negative reduced cost)
            entering = np.argmin(reduced_costs)
            if reduced_costs[entering] >= 0:
                raise ValueError("The LP problem is unbounded.")

            # Ratio test to find the leaving variable
            ratios = [
                tableau[i, -1] / tableau[i, entering] if tableau[i, entering] > 0 else np.inf
                for i in range(self.m)
            ]
            leaving = np.argmin(ratios)
            if ratios[leaving] == np.inf:
                raise ValueError("No valid pivots; problem may be infeasible.")

            # Pivot operation
            pivot_row(tableau, obj_row, leaving, entering)

            # Update the index of the basic variable
            cb_indices[leaving] = entering

        # Extract the solution
        solution = np.zeros(self.n)
        for i in range(self.m):
            if cb_indices[i] < self.n:
                solution[cb_indices[i]] = tableau[i, -1]
        optimal_value = np.dot(solution, self.c)

        return Solution(optimal_value=optimal_value, optimal_solution=solution.tolist())


def pivot_row(
    tableau: np.ndarray, obj_row: np.ndarray, pivot_row_index: int, pivot_col_index: int
) -> None:
    """
    Pivots the given row (in place) in the tableau using the specified pivot element.

    Args:
        tableau: The tableau representing the linear programming problem.
        obj_row: The objective row of the tableau.
        pivot_row_index: The index of the pivot row.
        pivot_col_index: The index of the pivot column.

    Returns:
        None
    """
    pivot_element = tableau[pivot_row_index, pivot_col_index]
    tableau[pivot_row_index, :] /= pivot_element
    for i in range(tableau.shape[0]):
        if i != pivot_row_index:
            ratio = tableau[i, pivot_col_index]
            tableau[i, :] -= ratio * tableau[pivot_row_index, :]
    ratio = obj_row[pivot_col_index]
    obj_row -= ratio * tableau[pivot_row_index, :]


def simplex() -> Solution:
    """
    Solves a linear programming problem using the Simplex method.

    Returns:
        The solution to the linear programming problem.
    """
    # Define the coefficients of the objective function
    c = LP_PROBLEM.c
    # Define the inequality constraints (Ax <= b)
    A = LP_PROBLEM.A
    b = LP_PROBLEM.b

    # Create a Simplex solver instance and solve
    solver = SimplexSolver(c=c, A=A, b=b)
    solution = solver.solve()

    return solution
