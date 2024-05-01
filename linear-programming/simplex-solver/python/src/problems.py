from pydantic import BaseModel


class Solution(BaseModel):
    """
    Represents the solution to a linear programming problem.

    Attributes:
        optimal_value: The optimal value of the objective function.
        optimal_solution: The optimal solution to the problem.
    """

    optimal_value: float
    optimal_solution: list[float]


class LPProblem(BaseModel):
    """
    Represents a linear programming problem.

    Attributes:
        c: The coefficients of the objective function.
        A: The coefficients of the inequality constraints.
        b: The right-hand side values of the inequality constraints.
        bounds: The lower and upper bounds for each variable.
        optimal_solution: The optimal solution to the problem.
    """

    c: list[float]
    A: list[list[float]]
    b: list[float]
    bounds: list[tuple[float | None, float | None]]
    optimal_solution: Solution


# Define a linear programming problem, including it's optimal solution (gotten from open source solver)
LP_PROBLEM = LPProblem(
    c=[20.0, 10.0],
    A=[[-1.0, -2.0], [-3.0, -1.0]],
    b=[-9.0, -6.0],
    bounds=[(0.0, None), (0.0, None)],
    optimal_solution=Solution(optimal_value=54.0, optimal_solution=[0.6, 4.2]),
)
