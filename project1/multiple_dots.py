import numpy as np
import os
import time
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree
from copy import deepcopy
mazef = open("mediumSearch.txt")
maze = mazef.readlines()
maze[len(maze)-1] = maze[len(maze)-1]+"\n"

from a_star_function import astar
import heapq
#from queue import PriorityQueue
class PriorityQueue:
    def __init__(self):
        self._queue = []
    def empty(self):
        return len(self._queue) == 0
    def put(self, obj):
        heapq.heappush(self._queue, (obj[0], obj[1]))
    def get(self):
        return heapq.heappop(self._queue)
start = time.clock()
path = []
g = []
s = ()
wall = []
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == '.':
            g.append((x,y))
        if maze[x][y] == '%':
            wall.append((x,y))
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == 'P':
            s = (x,y)
            break

def manhattanDistance(pos1, pos2):
    return abs(pos2[0]-pos1[0]) + abs(pos2[1]-pos1[1])

def get_astar_of_two_points(p1, p2):
    if(p1 == p2):
        return 0
    new_maze = []
    for i in range(len(maze)):
        new_maze_row = []        
        for j in range(len(maze[0])):
            new_maze_row.append(' ')
        new_maze_row.append('\n')
        temp_str = ''.join(new_maze_row)
        new_maze.append(temp_str)
    for i in wall:
        new_maze[i[0]] = new_maze[i[0]][:i[1]] + '%' + new_maze[i[0]][i[1]+1:]
    new_maze[p1[0]] = new_maze[p1[0]][:p1[1]] + 'P' + new_maze[p1[0]][p1[1]+1:]
    new_maze[p2[0]] = new_maze[p2[0]][:p2[1]] + '.' + new_maze[p2[0]][p2[1]+1:]
    #print(p1,p2)
    return astar(new_maze)

def get_bfs_of_two_points(p1, p2):
    if(p1 == p2):
        return 0
    new_maze = []
    for i in range(len(maze)):
        new_maze_row = []        
        for j in range(len(maze[0])):
            new_maze_row.append(' ')
        new_maze_row.append('\n')
        temp_str = ''.join(new_maze_row)
        new_maze.append(temp_str)
    for i in wall:
        new_maze[i[0]] = new_maze[i[0]][:i[1]] + '%' + new_maze[i[0]][i[1]+1:]
    new_maze[p1[0]] = new_maze[p1[0]][:p1[1]] + 'P' + new_maze[p1[0]][p1[1]+1:]
    new_maze[p2[0]] = new_maze[p2[0]][:p2[1]] + '.' + new_maze[p2[0]][p2[1]+1:]
    #print(p1,p2)
    return bfs(new_maze)

def get_goals_distances(goal_array):
    goal_distances_dict = {}
    for current_goal in goal_array:
        for target_goal in goal_array:
            if current_goal is not target_goal:
                dist = get_astar_of_two_points(current_goal, target_goal)
                goal_distances_dict[(current_goal, target_goal)] = dist
    return goal_distances_dict
            
parent = np.zeros((len(maze), len(maze[0])), dtype=tuple)
for x in range(len(parent)):
    for y in range(len(parent[0])):
        parent[x][y] = (0,0, 0, g)

init_g_distances = get_goals_distances(g)
def get_heuristic(goals_array, pacman_position):
    weighted_graph = []
    #pacman_distances_to_goals = [0]
    goals_distances_to_graph = []
    for goal in goals_array:
        #distance = get_astar_of_two_points(pacman_position, goal)
        #pacman_distances_to_goals.append(distance)
        goal_to_all_goals = [] #append distance to pacman's position as first element of each goal's array
        for target_goal in goals_array:
            if goal is not target_goal:
                goal_to_all_goals.append(init_g_distances[(goal, target_goal)])
            else:
                goal_to_all_goals.append(0)
        goals_distances_to_graph.append(goal_to_all_goals)
    #weighted_graph.append(pacman_distances_to_goals)
    weighted_graph += goals_distances_to_graph
    #print(weighted_graph)
    X = csr_matrix(weighted_graph)
    Tcsr = minimum_spanning_tree(X)
    tcsr_array = Tcsr.toarray()
    total = sum(map(sum,tcsr_array)) #from https://stackoverflow.com/questions/10713150/how-to-sum-a-2d-array-in-python
    return total

frontListAstar = PriorityQueue()
init_node = (s[0], s[1], 0, g)
history = []
frontListAstar.put((0, (s[0], s[1], 0, g, history))) #priority, (x,y,current_cost, current_g)
path = []
path.append((s[0],s[1], g))
solution = []
count = 0
tracker = len(g)
neighbors = [(0,1),(1,0),(0,-1),(-1,0)]
while not frontListAstar.empty():
    node =  frontListAstar.get()
    node = node[1]
    currX = node[0]
    currY = node[1]
    new_cost = node[2]
    currG = node[3]
    count += 1
    if (currX,currY) in currG:
        currG.remove((currX, currY))
        if(len(currG) < tracker):
            tracker = len(currG)
            print("Progress.. ",tracker, count)
        #path = []
    if (len(currG) == 0):
        print('found all')
        print('time elapsed = ', time.clock() - start)
        #print('hist = ', len(currH))
        solution = currH
        #print('nc = ', new_cost -1 )
        print('len of soln = ', len(solution))
        #print('parent = ', parent)
        #printPath(node, (s[0], s[1], 0, g), parent, maze, 0, count)
        break
    heur = 0
    currH = node[4]
    new_hist = []
    for neighbor in neighbors:
        x = currX + neighbor[0]
        y = currY + neighbor[1]
        if maze[x][y] != '%':
            if (x,y, currG) not in path:
                heur = get_heuristic(currG, (x, y))
                priority = new_cost + heur
                new_hist = deepcopy(currH)
                new_hist.append((x, y))
                frontListAstar.put((priority, (x, y , new_cost+1, deepcopy(currG), new_hist)))
                parent[x][y] = (currX,currY, new_cost, deepcopy(currG))
                path.append((x,y, currG))
            elif parent[x][y][2] > new_cost:
                heur = get_heuristic(currG, (x, y))
                priority = new_cost + heur
                new_hist = deepcopy(currH)
                new_hist.append((x, y))
                frontListAstar.put((priority, (x, y , new_cost+1, deepcopy(currG), new_hist)))
                parent[x][y] = (currX,currY, new_cost, deepcopy(currG))
f = open("solution_astar1,2.txt",'w')
f.writelines(maze)
for coord in solution:
    str1 = '(' + str(coord[0]) + ',' + str(coord[1]) + ')' '\n'
    f.writelines(str1)
for coord in solution:
    f.writelines(str(coord) + '\n')
f.writelines('cost = ' + str(len(solution)))
f.writelines('nodes expanded = ' + str(count))
f.close()