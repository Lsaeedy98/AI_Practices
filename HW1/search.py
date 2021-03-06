# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # test

    Frontier = util.Stack()
    Frontier.push((problem.getStartState(), []))

    # list of  explored nodes for checking
    Explored = []
    #Explored.append(problem.getStartState())

    while True:
        # next node in frontier
        tempState = Frontier.pop()
        state = tempState[0]
        actions = tempState[1]
        # add to explored so it can not be added to frontier again
        Explored.append(state)

        if (problem.isGoalState(state)):
            return actions

        # generate succesors and add them
        for next in problem.getSuccessors(state):
            new_state = next[0]
            new_direction = next[1]
            # add to frontier to generate its children in the next loop
            if new_state not in Explored:
                Frontier.push((new_state, actions + [new_direction]))
        # end of nodes in graph
        if Frontier.isEmpty() == 1:
            break
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    # next node in frontier queue
    Frontier = util.Queue()
    Frontier.push((problem.getStartState(), []))

    #make a list for explored nodes
    Explored = []

    while True:

        tempState = Frontier.pop()
        state = tempState[0]
        actions = tempState[1]
        # add to explored so it can not be added to frontier again


        if problem.isGoalState(state):
            # found goal
            return actions
        if state not in Explored:
            Explored.append(state)
            # generate succesors and add them
            for next in problem.getSuccessors(state):
                new_state = next[0]
                new_direction = next[1]
                #add to frontier to generate its children in the next loop
                Frontier.push((new_state, actions + [new_direction]))
        # end of nodes in graph
        if Frontier.isEmpty() == 1:
            break
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
#a list for states of nodes to check if a repeated state is being added, update the cost to lower one
    Frontier = []
    Frontier.append(problem.getStartState())

#priority queue of nodes and  path costs
    Queue = util.PriorityQueue()
    Queue.push((problem.getStartState(), []), 0)
#list of visited nodes
    Expanded = []

    while True:
        #next node in priority queue
        tempState = Queue.pop()
        state = tempState[0]
        actions = tempState[1]
        Frontier.remove(state)

        if (problem.isGoalState(state)):
            return actions

        if state not in Expanded:
            #expand node and generate children
            Expanded.append(state)
            for next in problem.getSuccessors(state):
                new_state = next[0]
                new_direction = next[1]
                #check frontier to have reapeated nodes - nodes in priority queue also exist in frontier
                if next not in Frontier:
                    Queue.push((new_state, actions + [new_direction]), problem.getCostOfActions(actions + [new_direction]))
                    Frontier.append(new_state)
                else:
                    Queue.update((new_state, actions + [new_direction]), problem.getCostOfActions(actions + [new_direction]))
        #end of nodes in graph
        if Queue.isEmpty()==1:
            break

    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # a list for states of nodes to check if a repeated state is being added, update the cost to lower one
    Frontier = []
    Frontier.append(problem.getStartState())

    # priority queue of nodes and  path costs
    Queue = util.PriorityQueue()
    #first node has no path cost so far and only has heuristic value
    Queue.push((problem.getStartState(), []), heuristic(problem.getStartState(),problem))
    # list of visited nodes
    Expanded = []

    while True:
        # next node in priority queue
        tempState = Queue.pop()
        state = tempState[0]
        actions = tempState[1]
        Frontier.remove(state)

        if (problem.isGoalState(state)):
            return actions

        if state not in Expanded:
            # expand node and generate children
            Expanded.append(state)
            for next in problem.getSuccessors(state):
                new_state = next[0]
                new_direction = next[1]
                # check frontier to have reapeated nodes - nodes in priority queue also exist in frontier
                if next not in Frontier:
                    Queue.push((new_state, actions + [new_direction]),
                                heuristic(new_state, problem)+problem.getCostOfActions(actions + [new_direction]))
                    Frontier.append(new_state)
                else:
                    Queue.update((new_state, actions + [new_direction]),
                                 heuristic(new_state, problem) + problem.getCostOfActions(actions + [new_direction]))
        # end of nodes in graph
        if Queue.isEmpty() == 1:
            break
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
