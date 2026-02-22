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
    
    x1, y1 = state
    x2, y2 = problem.goal
    distancia = abs(x1 - x2) + abs(y1 - y2)
    return distancia



def euclideanHeuristic(state, problem):
    """
    The Euclidean distance heuristic.
    """
    # TODO: Add your code here
    x1, y1 = state
    x2, y2 = problem.goal
    distancia = ((x1-x2)**2 + (y1-y2)**2)**0.5  
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

    position, survivors_grid = state
    
    survivors = survivors_grid.asList()
    
    if not survivors:
        return 0
    
   
    minDist = min(
        abs(position[0] - sx) + abs(position[1] - sy)
        for (sx, sy) in survivors
    )
    
    
    maxDist = 0
    for i in range(len(survivors)):
        x1, y1 = survivors[i]
        for j in range(i+1, len(survivors)):
            x2, y2 = survivors[j]
            dist = abs(x1 - x2) + abs(y1 - y2)
            if dist > maxDist:
                maxDist = dist
    
    return minDist + maxDist

