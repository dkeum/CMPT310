import sys
sys.path.append('../')
from search import Problem, Node, EightPuzzle
from random import *
#from tests.test_search import *
import time
from collections import deque
from utils import *




################### EIGHT PUZZLE 

def astar_search(problem, h=None, display=False, ):
    """A* search is best-first graph search with f(n) = g(n)+h(n).
    You need to specify the h function when you call astar_search, or
    else in your Problem subclass."""
    h = memoize(h or problem.h, 'h')
    return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display=True)


# A* heuristics 




# ________________________________________

def best_first_graph_search(problem, f, display=True):
    """Search the nodes with the lowest f scores first.
    You specify the function f(node) that you want to minimize; for example,
    if f is a heuristic estimate to the goal, then we have greedy best
    first search; if f is node.depth then we have breadth-first search.
    There is a subtlety: the line "f = memoize(f, 'f')" means that the f
    values will be cached on the nodes as they are computed. So after doing
    a best first search you can examine the f values of the path returned."""
    f = memoize(f, 'f')
    node = Node(problem.initial)
    
    frontier = PriorityQueue('min', f)
    frontier.append(node)
    explored = set()

    while frontier:
        node = frontier.pop()
        counter+=1
        if problem.goal_test(node.state):
            
            #print(len(explored), "paths have been expanded and", len(frontier), "paths remain in the frontier")
               
            return [len(explored),node]
        explored.add(node.state)
        for child in node.expand(problem):
            if child.state not in explored and child not in frontier:
                frontier.append(child)
            elif child in frontier:
                if f(child) < frontier[child]:
                    del frontier[child]
                    frontier.append(child)
    
    return None


#################################################







##################### Question 1 ############################
## Return solvable state ###
def make_rand_8puzzle():
    global state
    global solution
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    puzzle = EightPuzzle(tuple(state))
    new_puzzle = scramble_not_GUI(puzzle)    
    display(new_puzzle)
    puzzle = EightPuzzle(tuple(new_puzzle),tuple(state))
    
    solution = None
    
    is_solvable = puzzle.check_solvability(new_puzzle)
    
    # if the puzzle is not solvable then keep trying until there is a solvable puzzle
    if(is_solvable == False):
         while(is_solvable == False):
              puzzle = EightPuzzle(tuple(state))
              new_puzzle = scramble_not_GUI(puzzle)    
              display(new_puzzle)
              puzzle = EightPuzzle(tuple(new_puzzle),tuple(state)) 
              is_solvable = puzzle.check_solvability(new_puzzle)
             
    #case when puzzle works
    else:
        print("Your puzzle is solvable! \n")
    return puzzle
    

#print function for states
def display(state):
    for i in range(3):
        for j in range(3):
            if state[3*i+j] == 0:
                print('*', end=" ")
            else:
                print(state[3*i+j], end=" ")
        print()


    
## Helper function to scramble the states 
def scramble_not_GUI(puzzle):
    """Scrambles the puzzle starting from the goal state"""
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0] 
    possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    scramble = []
    for _ in range(60):
        scramble.append(random.choice(possible_actions))
        
        #randomly swaps the states
    for move in scramble:
        if move in puzzle.actions(state):
            state = list(puzzle.result(state, move))
            changed_puzzle = EightPuzzle(tuple(state))
    return state






#################### Question 2 ###################

def question_2_exe():
        puzzle = make_rand_8puzzle()  
        #running time check if it is ain seconds 
        start_time = time.time()
        solution = astar_search(puzzle) # Modfied function in search.py
        print("THIS IS THE Node Expanded: "+ str(solution[0]))
        elapsed_time = time.time()-start_time
        print("This is the total running time: " + str(elapsed_time) + " seconds")
        #length
        print("This is the length of the solution: " + str(len(solution[1].solution())) + "\n")


def question_2_with_input(state_input):
    state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    if len(state_input) == 9:
        puzzle = EightPuzzle(tuple(state_input[0:]),tuple(state))
        is_solvable = puzzle.check_solvability(tuple(state_input[0:]))         
             #case when puzzle works
        if(is_solvable == True):
            print("Your puzzle is solvable! \n")
            start_time = time.time()
            display(state_input)
            solution = astar_search(puzzle,h=puzzle.h) # Modfied function in search.py
            print("THIS IS THE Node Expanded: "+ str(solution[0]))            
            elapsed_time = time.time()-start_time
            print("This is the total running time: " + str(elapsed_time) + " seconds \n")
            #length
            print("This is the length of the solution: " + str(len(solution[1].solution())) + "\n")
        # if the puzzle is not solvable then keep trying until there is a solvable puzzle
        elif(is_solvable == False):
            print(" Your puzzle did not work\n")
    
    
def main():
    #question 2 
    new_list = list(map(int,sys.argv[1:]))
    if len(sys.argv) == 10:
        question_2_with_input(new_list)
    else: 
         question_2_exe()
    

################### Question 3 ########################

#n is a node 
def manhattan(n):
   
    sum = 0; 
    index_goal = {0: [2, 2], 1: [0, 0], 2: [1, 0], 3: [2, 0], 4: [0, 1], 5: [1, 1], 6: [2, 1], 7: [0, 2], 8: [1, 2]}
    index_state = {}
    index = [[0, 0], [1, 0], [2, 0], [0, 1], [1, 1], [2, 1], [0, 2], [1, 2], [2, 2]]
    
    #store the current numbers coordinates in a array
    for i in range(len(n.state)):
        index_state[n.state[i]] = index[i]
            
    # compare the distances and sum afterwards
    for i in range(9):
        x1,y1 = index_state[i] # store the coordinate
        x2,y2 = index_goal[i]       
        sum = abs(x2-x1) + abs(y2-y1) + sum
        # print("this is the sum from function: " + str(sum))
    index_state = {}  # reset this at the end of the iteration  
    return sum

    

    
################### Question 4 ########################


def gaschnig(n):    
    num_moves = 0
    
    # get the inital state
    # for n_state in n.path():
    #initial_state  = list(n.path()[0])
    initial_state  = list(n.state)
    #print("this is the initial state")
    #print(initial_state)
    goal_state = [1,2,3,4,5,6,7,8,0]
    
    while initial_state != goal_state:
        #get the index at zero and swap with any misplaced tiles
        index_zero = initial_state.index(0)
        if initial_state[8] != 0:
            num_1 = goal_state[index_zero] # the number that belong in the spot
            num_2 = initial_state.index(num_1)
            initial_state[index_zero] = num_1
            initial_state[num_2] = 0
        else:
            for i in range(9):
                if initial_state[i] != goal_state[i]:
                    temp_1 = initial_state[i] 
                    initial_state[i] = 0
                    initial_state[8] = temp_1
                    break;
        #print(initial_state)       
        num_moves= num_moves+1
        
    #print(num_moves)    
    return num_moves






################### Question 5 ########################
def create_10_puzzles():
    
   #display(puzzle.state)
    for i in range(10):
        puzzle = make_rand_8puzzle()
        start_time = time.time()
        solution = astar_search(puzzle) # Modfied function in search.py
        elapsed_time = time.time()-start_time       
        # display the initial state
        
        print("Misplaced Tile Heuristic")
        print("THIS IS THE Node Expanded: "+ str(solution[0]))            
        print("This is the total running time: " + str(elapsed_time) + " seconds \n")
        print("This is the length of the solution: " + str(len(solution[1].solution())) + "\n")
        
        start_time = time.time()
        solution = astar_search(puzzle, h=manhattan) # Modfied function in search.py
        elapsed_time = time.time()-start_time
        print("Manhattan Heuristic")
        print("THIS IS THE Node Expanded: "+ str(solution[0]))            
        print("This is the total running time: " + str(elapsed_time) + " seconds \n")
        print("This is the length of the solution: " + str(len(solution[1].solution())) + "\n")
        
        start_time = time.time()
        solution = astar_search(puzzle, h=gaschnig) # Modfied function in search.py
        elapsed_time = time.time()-start_time
        print("Gaschnig Heuristic")
        print("THIS IS THE Node Expanded: "+ str(solution[0]))            
        print("This is the total running time: " + str(elapsed_time) + " seconds \n")
        print("This is the length of the solution: " + str(len(solution[1].solution())) + "\n")
        print("----------------------------------------------------------------------------------")



###### for Question 1,2 ######
main() 


###### for Question 3,4,5 #####
create_10_puzzles() # comment if you do not like the program to generate 10 puzzles







