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
        costoMinNodo = None
        costoMinState = None
        
        for child in problem.getSuccessors(nodo):
            
            state = child[0]
            
            if problem.isGoalState(state):
                return child
            if (child[2] < costoMin):## and (state not in reached):
                   costoMin = child[2]
                   costoMinNodo = child
                   costoMinState = state
        if costoMinState in acciones:
            acciones.append(costoMinState)
            frontier.push(costoMinNodo)
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
            
        
        
        


# Abbreviations (you can use them for the -f option in main.py)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
