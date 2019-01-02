import numpy as np
mazef = open("mediumMaze.txt")
maze = mazef.readlines()
maze[len(maze)-1] = maze[len(maze)-1]+"\n"

from queue import PriorityQueue 

class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter += 1

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item

# In[5]:

parent = np.zeros((len(maze), len(maze[0])), dtype=tuple)
path = []
g = ()
s = ()
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == '.':
            g = (x,y)
            break
for x in range(len(maze)):
    for y in range(len(maze[0])):
        if maze[x][y] == 'P':
            s = (x,y)
            break
            
def printPath (currNode, startNode, plist, maze, n, c):
    prev = plist[currNode[0]][currNode[1]]
    print(prev)
    if prev == startNode:
        f = open("greedy_bfs_solution.txt",'w')
        f.writelines(maze)
        f.write(str(n)+',')
        f.write(str(c))
        f.close()
        return
    maze[prev[0]] = maze[prev[0]][:prev[1]] + '-' + maze[prev[0]][prev[1]+1:]
    printPath(prev, startNode, plist, maze, n+1, c)

def manhattanDistance(pos1, pos2):
    return abs(pos2[0]-pos1[0]) + abs(pos2[1]-pos1[1])


parent = np.zeros((len(maze), len(maze[0])), dtype=tuple)
path = []
frontListBFS = MyPriorityQueue()
frontListBFS.put(s, 0)
path.append(s)
count = 0
while not frontListBFS.empty():
    count += 1
    node = frontListBFS.get()
    if node == g:
        print("Found!")
        printPath(node, s, parent, maze, 0, count)
        break
    currX = node[0]
    currY = node[1]
    dist = 0
    if maze[currX][currY+1] != '%' and (currX,currY+1) not in path:
        dist = manhattanDistance(g, (currX, currY+1))
        frontListBFS.put((currX, currY+1),dist)
        parent[currX][currY+1] = (currX,currY)
        path.append((currX,currY+1))
    if maze[currX+1][currY] != '%' and (currX+1,currY) not in path:
        dist = manhattanDistance(g, (currX+1, currY))
        frontListBFS.put((currX+1, currY), dist)
        parent[currX+1][currY] = (currX,currY)
        path.append((currX+1,currY))
    if maze[currX][currY-1] != '%' and (currX,currY-1) not in path:
        dist = manhattanDistance(g, (currX, currY-1))
        frontListBFS.put((currX, currY-1), dist)
        parent[currX][currY-1] = (currX,currY)
        path.append((currX,currY-1))
    if maze[currX-1][currY] != '%' and (currX-1,currY) not in path:
        dist = manhattanDistance(g, (currX-1, currY))
        frontListBFS.put((currX-1, currY), dist)
        parent[currX-1][currY] = (currX,currY)
        path.append((currX-1,currY))