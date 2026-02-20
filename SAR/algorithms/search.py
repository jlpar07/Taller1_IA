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
    inicio = problem.getStartState()
    pila.push(inicio)
    visitados = set()
    acciones = []
    #acciones.append(inicio[1])
    
    while not pila.isEmpty():
        nodo = pila.pop()
        if problem.isGoalState(nodo):
            return acciones
        if nodo in visitados:
            continue
        visitados.add(nodo)
        for hijo in problem.getSuccessors(nodo):   #toca agregarle las restricciones de movimiento al parecer, en algunos casos tira excepción de movimiento ilegal
            #if RescueState.getLegalActions(hijo[0]).count(hijo[1]) > 0: #se verifica que la acción sea legal para el estado actual
                pila.push(hijo[0])  #hijo[0] es el estado sucesor, hijo[1] es la acción, hijo[2] es el costo
                acciones.append(hijo[1])
    
    return None


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
    Search the node that has the lowest combined cost and heuristic first.
    """
    # TODO: Add your code here
    inicio = problem.getStartState()
    novisitados = utils.PriorityQueue()
    novisitados.push(inicio, heuristic(inicio, problem))
    visitados = set()
    while novisitados:
        nodo = novisitados.pop()  #nodo es el estado actual
        if problem.isGoalState(nodo):
            return nodo
        visitados.add(nodo)
        for vecino in problem.getSuccessors(nodo):
            if vecino in visitados:
                continue
            costo = nodo[2] + heuristic(vecino,problem)  # nodo[2] es el costo del movimiento
            if vecino not in novisitados:
                novisitados.push(vecino,costo)
            #elif costo < novisitados.getPriority(vecino[0]): #si el costo es menor que el costo actual en la cola de prioridad, se actualiza el costo
                #visitados.update(vecino, costo)
    return None

def aStar(problem: SearchProblem, heuristic):
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
aStar2 = aStar
