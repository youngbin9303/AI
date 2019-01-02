
# coding: utf-8

# In[21]:

import numpy as np
mazef = open("openMaze.txt")
maze = mazef.readlines()
maze[len(maze)-1] = maze[len(maze)-1]+"\n"


# In[22]:

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
            
def printPath (currNode, startNode, plist, maze):
    
    prev = plist[currNode[0]][currNode[1]]
    if prev == startNode:
        f = open("solution.txt",'w')
        f.writelines(maze)
        f.close()
        return
    maze[prev[0]] = maze[prev[0]][:prev[1]] + '-' + maze[prev[0]][prev[1]+1:]
    printPath(prev, startNode, plist, maze)


# In[20]:

# DFS solution

parent = np.zeros((len(maze), len(maze[0])), dtype=tuple)
path = [s]
frontListDFS = [s]
count = 0
while frontListDFS != []:
    count += 1
    node = frontListDFS.pop()
    if node == g:
        #print("Found!")
        printPath(node, s, parent, maze)
        break
    currX = node[0]
    currY = node[1]
    if maze[currX][currY+1] != '%' and (currX,currY+1) not in path:
        frontListDFS.append((currX, currY+1))
        parent[currX][currY+1] = (currX,currY)
        path.append((currX,currY+1))
    if maze[currX+1][currY] != '%' and (currX+1,currY) not in path:
        frontListDFS.append((currX+1, currY))
        parent[currX+1][currY] = (currX,currY)
        path.append((currX+1,currY))
    if maze[currX][currY-1] != '%' and (currX,currY-1) not in path:
        frontListDFS.append((currX, currY-1))
        parent[currX][currY-1] = (currX,currY)
        path.append((currX,currY-1))
    if maze[currX-1][currY] != '%' and (currX-1,currY) not in path:
        frontListDFS.append((currX-1, currY))
        parent[currX-1][currY] = (currX,currY)
        path.append((currX-1,currY))


# In[23]:

# BFS solution 
import queue as Q
parent = np.zeros((len(maze), len(maze[0])), dtype=tuple)
path = []
frontListBFS = Q.Queue()
frontListBFS.put(s)
path.append(s)
while not frontListBFS.empty():
    count += 1
    node = frontListBFS.get()
    if node == g:
        #print("Found!")
        printPath(node, s, parent, maze)
        break
    currX = node[0]
    currY = node[1]
    if maze[currX][currY+1] != '%' and (currX,currY+1) not in path:
        frontListBFS.put((currX, currY+1))
        parent[currX][currY+1] = (currX,currY)
        path.append((currX,currY+1))
    if maze[currX+1][currY] != '%' and (currX+1,currY) not in path:
        frontListBFS.put((currX+1, currY))
        parent[currX+1][currY] = (currX,currY)
        path.append((currX+1,currY))
    if maze[currX][currY-1] != '%' and (currX,currY-1) not in path:
        frontListBFS.put((currX, currY-1))
        parent[currX][currY-1] = (currX,currY)
        path.append((currX,currY-1))
    if maze[currX-1][currY] != '%' and (currX-1,currY) not in path:
        frontListBFS.put((currX-1, currY))
        parent[currX-1][currY] = (currX,currY)
        path.append((currX-1,currY))


# In[ ]:


