from numpy import inf
from algorithms.problems import SearchProblem
import algorithms.utils as utils
from world.game import Directions
from algorithms.heuristics import nullHeuristic


def tinyHouseSearch(problem: SearchProblem):
    """
    Returns a sequence of moves that solves tinyHouse. For any other building, the
    sequence of moves will be incorrect, so only use this for tinyHouse.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # TODO: Add your code here
    pila = utils.Stack()
    inicio = problem.getStartState()
    pila.push(inicio)
    visitados = set()
    acciones = []
    
    while not pila.isEmpty():
        nodo = pila.pop()
        if problem.isGoalState(nodo):
            return acciones
        if nodo in visitados:
            continue
        visitados.add(nodo)
        for hijo in problem.getSuccessors(nodo):   #toca agregarle las restricciones de movimiento al parecer, en algunos casos tira excepción de movimiento ilegal
            pila.push(hijo[0])  #hijo[0] es el estado sucesor, hijo[1] es la acción, hijo[2] es el costo
            acciones.append(hijo[1])
    
    return acciones
   


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    frontier = utils.Stack()
    inicio = problem.getStartState()
    frontier.push(inicio)
    reached = set()
    acciones = []
    if inicio == problem.isGoalState():
        return acciones
    while not frontier.isEmpty():
        nodo = frontier.pop()
        costoMin = inf
        
        for child in problem.getSuccessors(nodo):
            state = child[0]
            ##frontier.push(child[0])
            if problem.isGoalState(state):
                return child
            if child[0] in acciones:
                acciones.append(state)
                frontier.push(child)
    acciones[0] = -1
    return acciones










    node = problem.getStartState()
    if node == problem.isGoalState(node):
        return []
    priorityQueue = utils.PriorityQueue()
    frontier = utils.PriorityQueue()
    funcPriotyGueue = utils.PriorityQueueWithFunction(lambda n: problem.getCostOfActions(n[1]) + heuristic(n[0], problem))


    utils.raiseNotDefined()



def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    utils.raiseNotDefined()


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
