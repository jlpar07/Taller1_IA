from typing import Any, Tuple
from algorithms import utils
from algorithms.problems import MultiSurvivorProblem
from algorithms.problems import SimpleSurvivorProblem


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def manhattanHeuristic(state, problem):
    """
    The Manhattan distance heuristic.
    """
    # TODO: Add your code here
    inicio = problem.getStartState()   # mmm no lo sé
    distancia = abs((state[0][0]-inicio[0][0]) + (state[0][1]-inicio[0][1]))
    ##no sé si haya que poner algo más
    return distancia



def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    inicio = problem.getStartState()   # mmm no lo sé
    distancia = ((state[0][0]-inicio[0][0])**2 + (state[0][1]-inicio[0][1])**2)**0.5  
    ##no sé si haya que poner algo más
    return distancia


def survivorHeuristic(state: Tuple[Tuple, Any], problem: MultiSurvivorProblem):
    """
    Your heuristic for the MultiSurvivorProblem.

    state: (position, survivors_grid)
    problem: MultiSurvivorProblem instance

    This must be admissible and preferably consistent.

    Hints:
    - Use problem.heuristicInfo to cache expensive computations
    - Go with some simple heuristics first, then build up to more complex ones
    - Consider: distance to nearest survivor + MST of remaining survivors
    - Balance heuristic strength vs. computation time (do experiments!)
    """
    # TODO: Add your code here
    utils.raiseNotDefined()
