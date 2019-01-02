import numpy as np
mazef = open("bigMaze.txt")
maze = mazef.readlines()
maze[len(maze)-1] = maze[len(maze)-1]+"\n"

parent = np.zeros((len(maze), len(maze[0])), dtype=tuple)
path = []
g = ()
s = ()
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == '.':
            g = ((x,y),0)
            break
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == 'P':
            s = ((x,y),0)
            break
            
def printPath (currNode, startNode, plist, maze, n, c):
    n+=1
    prev = plist[currNode[0]][currNode[1]]
   # print(prev)
    if prev == startNode:
        f = open("solution_astar.txt",'w')
        f.writelines(maze)
        f.write(str(n)+',')
        f.write(str(c))
        f.close()
        return
    maze[prev[0]] = maze[prev[0]][:prev[1]] + '-' + maze[prev[0]][prev[1]+1:]
    printPath(prev, startNode, plist, maze, n, c)


def manhattanDistance(pos1, pos2):
    return abs(pos2[0]-pos1[0]) + abs(pos2[1]-pos1[1])
    
    
    
import queue as Q
parent = np.zeros((len(maze), len(maze[0])), dtype=tuple)
frontListAstar = Q.PriorityQueue()
frontListAstar.put((0, s))
path = []
path.append(s[0])
count = 0
while not frontListAstar.empty():
    count += 1
    node_mm = frontListAstar.get()
    node_m = node_mm[1]
    node = node_m[0]
    # print(node_m, g[0])
    if node == g[0]:
        #print("Found!")
        printPath(node, s[0], parent, maze, 0, count)
        break
    currX = node[0]
    currY = node[1]
    heur = 0
    new_cost = node_m[1] + 1
    
    if maze[currX][currY+1] != '%' and (currX,currY+1) not in path:
        heur = manhattanDistance(g[0], (currX, currY+1))
        priority = new_cost + heur
        frontListAstar.put((priority,((currX, currY+1),new_cost)))
        parent[currX][currY+1] = (currX,currY)
        path.append((currX,currY+1))
    if maze[currX+1][currY] != '%' and (currX+1,currY) not in path:
        heur = manhattanDistance(g[0], (currX+1, currY))
        priority = new_cost + heur
        frontListAstar.put((priority, ((currX+1, currY), new_cost)))
        parent[currX+1][currY] = (currX,currY)
        path.append((currX+1,currY))
    if maze[currX][currY-1] != '%' and (currX,currY-1) not in path:
        heur = manhattanDistance(g[0], (currX, currY-1))
        priority = new_cost + heur
        frontListAstar.put((priority, ((currX, currY-1), new_cost)))
        parent[currX][currY-1] = (currX,currY)
        path.append((currX,currY-1))
    if maze[currX-1][currY] != '%' and (currX-1,currY) not in path:
        heur = manhattanDistance(g[0], (currX-1, currY))
        priority = new_cost + heur
        frontListAstar.put((priority,((currX-1, currY), new_cost)))
        parent[currX-1][currY] = (currX,currY)
        path.append((currX-1,currY))