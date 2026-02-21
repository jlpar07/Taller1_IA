from numpy import inf
from world.rescue_state import RescueState
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
    acciones = []
    pila.push((problem.getStartState(), acciones))
    visitados = set()
    
    while not pila.isEmpty():
        estado, acciones = pila.pop()
        if problem.isGoalState(estado):
            return acciones
        if estado not in visitados:
            visitados.add(estado)
            for hijo in problem.getSuccessors(estado): 
                nuevo_camino = acciones + [hijo[1]]  #hijo[1] es la acción
                pila.push((hijo[0], nuevo_camino))   #hijo[0] es el estado sucesor, hijo[1] es la acción, hijo[2] es el costo
    return None


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    cola = utils.Queue()   # en BFS usamos cola en vez de pila
    acciones = []
    cola.push((problem.getStartState(), acciones))
    visitados = set()

    while not cola.isEmpty():
        estado, acciones = cola.pop()

        if problem.isGoalState(estado):
            return acciones

        if estado not in visitados:
            visitados.add(estado)
            for hijo in problem.getSuccessors(estado):
                nuevo_camino = acciones + [hijo[1]]  # hijo[1] es la accion
                cola.push((hijo[0], nuevo_camino))   # hijo[0] estado sucesor

    return None


def uniformCostSearch(problem: SearchProblem):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    inicio = problem.getStartState()

    
    acciones = []
    if problem.isGoalState(inicio):
        return None
    frontier = utils.PriorityQueue()

    reached = set()
    reached.add(inicio)
    costoAcumulado = 0
    frontier.push((inicio,acciones, costoAcumulado),0)

    bestCost = {inicio:0}

    while not frontier.isEmpty():

        (state, path, cost) = frontier.pop()

        if problem.isGoalState(state):
           return path
        
        if cost > bestCost[state]:
            continue

        
        for (succState, action, stepCost) in problem.getSuccessors(state):
            
            newCost = cost + stepCost
            newPath = path + [action]
            if succState not in bestCost or newCost < bestCost[succState]:
                bestCost[succState] = newCost
                frontier.push((succState, newPath,newCost), priority=newCost)
        
    return None

def aStarSearch(problem: SearchProblem, heuristic):
    """
    Search the node of least total cost first.
    """

    # TODO: Add your code here
    inicio = problem.getStartState()

    
    acciones = []
    if problem.isGoalState(inicio):
        return None
    frontier = utils.PriorityQueue()

    reached = set()
    reached.add(inicio)
    costoAcumulado = 0
    frontier.push((inicio,acciones, costoAcumulado),0)

    bestCost = {inicio:0}

    while not frontier.isEmpty():

        (state, path, cost) = frontier.pop()

        if problem.isGoalState(state):
           return path
        
        if cost > bestCost[state]:
            continue

        
        for (succState, action, stepCost) in problem.getSuccessors(state):
            
            newCost = cost + stepCost
            newPath = path + [action]
            if succState not in bestCost or newCost < bestCost[succState]:
                bestCost[succState] = newCost
                costHeuristic = heuristic(succState, problem)
                priorityFunc = newCost + costHeuristic
                frontier.push((succState, newPath,newCost), priorityFunc)
        
    return None
            
        
        
        


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
