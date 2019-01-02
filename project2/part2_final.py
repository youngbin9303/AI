import copy
import random

player = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
computer = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

stones = [[],[]]
stones[0] = player
stones[1] = computer
nodes_expand = [[],[]]



def opponent(player):
    if player == 1:
        return 0
    else:
        return 1

def isMine(s, player):
    if s in stones[player]:
        return True
    return False

def posState(board, x, y, player):
    if board[x][y]==' ':
        return '0'
    if isMine(board[x][y], player):
        return '1'
    return '2'

def has2(state):
    count = 0
    count_opponent = 0
    for i in range(1, 5):
        if state[i] == '2':
            return False
    for i in range(len(state)):
        if state[i] == '1':
            count += 1
        if state[i] == '2':
            count_opponent += 1
            if count_opponent > 1:
                return False
    if count == 2:
        return True
    return False

def has1(state):
    for i in range(1, 5):
        if state[i] == '2':
            return False
    count_opponent = 0
    for i in range(len(state)):
        if state[i] == '2':
            count_opponent += 1
            if count_opponent == 2:
                return False
        if state[i] == '1':
            return True
    return False

open3 = ['011100', '001110', '201110', '011102']
capped3 = ['111000', '211100', '201110', '200111', '000111', '001112', '011102', '111002']
open4 = ['011110']
capped4 = ['111100', '211110', '011112', '001111', '111102', '201111']
cons5 = ['111110', '011111', '111112', '211111']
gap4 = ['011011', '110110', '110112', '211011', '010111', '210111', '101110', '101112',
        '011101', '211101', '111010', '111012']
gap3 = ['010101', '210101', '101010', '101012',
        '011001', '211001', '110010', '110012',
        '010011', '210011', '100110', '100112',
        '010110', '210110', '101100', '101102',
        '011010', '211010', '110100', '110102',
        '001101', '201101', '011010', '011012',
        '001011', '201011', '010110', '010112']

open3_op = ['022200', '002220', '102220', '022201']
capped4_op = ['222200', '122220', '022221', '002222', '102222', '222201']
gap4_op = ['022022', '220220', '220221', '122022', '020222', '120222', '202220', '202221',
        '022202', '122202', '222020', '222021']

cons5_op = ['222220', '022222', '222221', '122222']
close4 = capped4 + gap4
close3 = capped3 + gap3
close4_op = capped4_op + gap4_op

def evalpattern(state):
    if state in cons5_op:
        return -10000000
    if state in cons5:
        return 100000
    if state in close4_op:
        return -100000
    if state in open4:
        return 10000
    if state in close4:
        return 1080
    if state in open3_op:
        return -5080
    if state in open3:
        return 1000
    if state in close3:
        return 100
    if has2(state):
        return 10
    if has1(state):
        return 1
    return 0

def evalboard(player, board):
    value = 0
    # horizontal blocks
    for i in range (0, 7):
        for j in range(0, 2):
            state = ''
            for k in range (j, j+6):
                state += posState(board, i, k, player)
            value += evalpattern(state)
    # vertical
    for i in range (0, 7):
        for j in range(0, 2):
            state = ''
            for k in range (j, j+6):
                state += posState(board, k, i, player)
            value += evalpattern(state)
    # top-left diagonal - mid
    for i in range(0, 2):
        state = ''
        for j in range(i, i+6):
            state += posState(board, j, j, player)
        value += evalpattern(state)
    # top-left diagonal - left
    for i in range(0, 1):
        state = ''
        for j in range(0,6):
            state += posState(board, j, j+1, player)
        value += evalpattern(state)
    # top-left diagonal - right
    for i in range(0, 1):
        state = ''
        for j in range(0,6):
            state += posState(board, j+1, j, player)
        value += evalpattern(state)
    # bottom-left diagonals
    for i in range(0, 2):
        state = ''
        for j in range(i, i+6):
            state += posState(board, 6-j, j, player)
        value += evalpattern(state)
            
    for i in range(0, 1):
        state = ''
        for j in range(0,6):
            state += posState(board, 6-j, j+1, player)
        value += evalpattern(state)
            
    for i in range(0, 1):
        state = ''
        for j in range(0,6):
            state += posState(board, 5-j, j, player)
        value += evalpattern(state)
    return value

def minimum_3(board, mine):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == mine:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+3, j+3))

                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == mine:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))



                #rule 4 horizontal
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == mine:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == mine:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                    v.append((i, j+1))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                    v.append((i, j+2))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))


                #rule 4 vertical
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == mine:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+3, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == mine:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                    v.append((i+1, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                    v.append((i+2, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))


                #rule 4 dia2
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+4, j-4))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+2, j-2))

        break
        
    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)

def minimum_2(board, mine):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == mine:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))


                #rule 4 horizontal
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == mine:
                    v.append((i, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))

                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))




                #rule 4 vertical
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == mine:
                    v.append((i+2, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))

                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))


                #rule 4 dia2
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+4, j-4))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))


        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)


def minimum_1(board, mine):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                    v.append((i+3, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == mine and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                    v.append((i, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == mine and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                    v.append((i+3, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == mine and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine and j >= 5:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == mine and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i, j))
                if whos(copy, i, j) == mine and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+1, j-1))
        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)


def reflex(board, player):

    if player == 0:
        mine = 1
        your = 0
    else:
        mine = 0
        your = 1

    copy = getBoardCopy(board)

    for i in range(0,7):
        for j in range(0,7):
            if whos(copy, i, j) == mine:
                #not first time
                fl = 1
                break
            else:
                fl = 0
                continue
        if fl == 1:
            break
#   if (check_four(board))[0] == -1:
    if fl == 0:
        while True:
            x = random.randint(0,6)
            y = random.randint(0,6)
            if whos(copy, x, y) == 2:
                return(x,y)


            #if whos(copy, x, y) == 2:
                #break



    if fl == 1:
        while True:
            for i in range(7):
                for j in range(7):

                    if whos(copy, i, j) == mine and whos(copy, i, j+1) == 2 and whos(copy, i, j+2) == mine and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == mine:
                        return(i, j+1)
                    if whos(copy, i, j) == mine and whos(copy, i, j+1) == mine and whos(copy, i, j+2) == 2 and whos(copy, i, j+3) == mine and whos(copy, i, j+4) == mine:
                        return(i, j+2)
                    if whos(copy, i, j) == mine and whos(copy, i, j+1) == mine and whos(copy, i, j+2) == mine and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == mine:
                        return(i, j+3)   
                    if whos(copy, i, j) == mine and whos(copy, i, j+1) == mine and whos(copy, i, j+2) == mine and whos(copy, i, j+3) == mine:
                        if whos(copy, i, j-1) == 2 and whos(copy, i, j+4) == 2 and j>=1:
                            return(i, j-1)
                        if whos(copy, i, j-1) == 2 and j>=1:
                            return(i, j-1)
                        if whos(copy, i, j+4) == 2:
                            return(i, j+4)

                    if whos(copy, i, j) == mine and whos(copy, i+1, j) == 2 and whos(copy, i+2, j) == mine and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == mine:
                        return(i+1, j)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j) == mine and whos(copy, i+2, j) == 2 and whos(copy, i+3, j) == mine and whos(copy, i+4, j) == mine:
                        return(i+2, j)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j) == mine and whos(copy, i+2, j) == mine and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == mine:
                        return(i+3, j)  
                    if whos(copy, i, j) == mine and whos(copy, i+1, j) == mine and whos(copy, i+2, j) == mine and whos(copy, i+3, j) == mine:
                        if whos(copy, i-1, j) == 2 and whos(copy, i+4, j) == 2 and i>=1:
                            return(i-1, j)
                        if whos(copy, i-1, j) == 2 and i>=1:
                            return(i-1, j)
                        if whos(copy, i+4, j) == 2:
                            return(i+4, j)

                    if whos(copy, i, j) == mine and whos(copy, i+1, j+1) == 2 and whos(copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == mine:
                        return(i+1, j+1)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j+1) == mine and whos(copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == mine and whos(copy, i+4, j+4) == mine:
                        return(i+2, j+2)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j+1) == mine and whos(copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == mine:
                        return(i+3, j+3)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j+1) == mine and whos(copy, i+2, j+2) == mine and whos(copy, i+3, j+3) == mine:
                        if whos(copy, i-1, j-1) == 2 and whos(copy, i+4, j+4) == 2 and j>=1 and i>=1:
                            return(i-1, j-1)
                        if whos(copy, i-1, j-1) == 2 and j>=1 and i>=1:
                            return(i-1, j-1)
                        if whos(copy, i+4, j+4) == 2:
                            return(i+4, j+4)

                    if whos(copy, i, j) == mine and whos(copy, i+1, j-1) == mine and whos(copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == mine:
                        return(i+3, j-3)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j-1) == mine and whos(copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == mine:
                        return(i+2, j-2)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j-1) == 2 and whos(copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == mine and whos(copy, i+4, j-4) == mine:
                        return(i+1, j-1)
                    if whos(copy, i, j) == mine and whos(copy, i+1, j-1) == mine and whos(copy, i+2, j-2) == mine and whos(copy, i+3, j-3) == mine and j >= 4:
                        if whos(copy, i-1, j+1) == 2 and whos(copy, i+4, j-4) == 2 and i>=1:
                            return(i-1, j+1)
                        if whos(copy, i-1, j+1) == 2 and i>=1:
                            return(i-1, j+1)
                        if whos(copy, i+4, j-4) == 2:
                            return(i+4, j-4)
                    else:
                        fl = 2
            break            



    if fl == 2:
        while True:
            for i in range(7):
                for j in range(7):
                    #3 in a row horizontal
                    if whos(copy, i, j) == your and whos(copy, i, j+1) == your and whos(copy, i, j+2) == your and whos(copy, i, j+3) == your:
                        if whos(copy, i, j-1) == 2 and j>=1:
                            return (i, j-1)
                        if whos(copy, i, j+4) == 2:
                            return (i, j+4)

                        #4th one came up and j<=2?

                    #3 in a row vertical
                    if whos(copy, i, j) == your and whos(copy, i+1, j) == your and whos(copy, i+2, j) == your and whos(copy, i+3, j) == your:
                        #4th one came up and i<=2 ?
                        if whos(copy, i-1, j) == 2 and i>=1:
                            return (i-1,j)
                        if whos(copy, i+4, j) == 2:
                            return (i+4,j)

                    #vertical 2
                    if whos(copy, i, j) == your and whos(copy, i+1, j+1) == your and whos(copy, i+2, j+2) == your and whos(copy, i+3, j+3) == your:
                        if whos(copy, i-1, j-1) == 2 and i>=1 and j>=1:
                            return (i-1,j-1)
                        if whos(copy, i+4, j+4) == 2:
                            return (i+4,j+4)


                    if whos(copy, i, j) == your and whos(copy, i+1, j-1) == your and whos(copy, i+2, j-2) == your and whos(copy, i+3, j-3) == your and j >= 4:
                        if whos(copy, i-1, j+1) == 2 and i>=1:
                            return (i-1,j+1)
                        if whos(copy, i+4, j-4) == 2:
                            return (i+4,j-4)


                    else:
                        fl = 3
            break


    if fl == 3:
        while True:
            for i in range(7):
                for j in range(7):
                    if whos(copy, i, j) == your and whos(copy, i, j+1) == your and whos(copy, i, j+2) == your and whos(copy, i, j-1) == 2 and whos(copy, i, j+3) == 2 and j>=1:
                        return (i,j-1)
                    if whos(copy, i, j) == your and whos(copy, i+1, j) == your and whos(copy, i+2, j) == your and whos(copy, i-1, j) == 2 and whos(copy, i+3, j) == 2 and i>=1:
                        return (i-1,j)
                    if whos(copy, i, j) == your and whos(copy, i+1, j+1) == your and whos(copy, i+2, j+2) == your and whos(copy, i-1, j-1) == 2 and whos(copy, i+3, j+3) == 2 and i>=1 and j>=1:
                        return (i-1,j-1)
                    if whos(copy, i, j) == your and whos(copy, i+1, j-1) == your and whos(copy, i+2, j-2) == your and whos(copy, i-1, j+1) == 2 and whos(copy, i+3, j-3) == 2 and  i>= 1:
                        return (i+3,j-3)
                    else:
                        fl = 4
            break


    if fl == 4:
        c = minimum_3(board, mine)
        if c == (-1, -1):
            fl = 5
        else:
            return (c)

    if fl == 5:
        b = minimum_2(board, mine)
        if b == (-1, -1):
            fl = 6
        else:
            return (b)



    if fl == 6:
        a = minimum_1(board, mine)
        if a == (-1,-1):
            fl = 7
        else:
            return (a)

    if fl == 7:
        for a in range(7):
            for b in range(7):
                if whos(copy, a, b) == 2:
                    return(a,b)

def minimax(board, player):
    openPos = []
    for i in range(len(board)):
        for j in range (len(board[0])):
            if board[i][j] == ' ':
                openPos.append((i,j))
    curr_best_move = openPos[0]
    curr_best_val = 0
    nodes_expanded = 0
    for i in range(len(openPos)):
        nodes_expanded += 1
        max_move_1 = openPos[i]
        openPos2 = copy.deepcopy(openPos)
        openPos2.remove(max_move_1)
        par_val = 0
        for j in range(len(openPos2)):
            nodes_expanded += 1
            min_move = openPos2[j]
            openPos3 = copy.deepcopy(openPos2)
            openPos3.remove(min_move)
            par_val2 = 100000000
            for k in range(len(openPos3)):
                nodes_expanded += 1
                max_move_2 = openPos3[k]
                tboard = copy.deepcopy(board)
                tboard[max_move_1[0]][max_move_1[1]] = stones[player][0]
                tboard[min_move[0]][min_move[1]] = stones[opponent(player)][0]
                tboard[max_move_2[0]][max_move_2[1]] = stones[player][0]
                bval = evalboard(player,tboard)
                if bval < par_val2:
                    par_val2 = bval
            if par_val2 > par_val:
                par_val = par_val2
        if par_val > curr_best_val:
            curr_best_val = par_val
            curr_best_move = max_move_1
    nodes_expand[player].append(nodes_expanded)
    print('nodes expanded = ', nodes_expanded)

    return curr_best_move

def alphabeta(board, player):
    alpha = float("-inf")
    beta = float("inf")
    openPos = []
    for i in range(len(board)):
        for j in range (len(board[0])):
            if board[i][j] == ' ':
                openPos.append((i,j))
    curr_best_move = openPos[0]
    curr_best_val = 0
    nodes_expanded = 0
    par_val = float("-inf")
    for i in range(len(openPos)):
        nodes_expanded += 1
        max_move_1 = openPos[i]
        openPos2 = copy.deepcopy(openPos)
        openPos2.remove(max_move_1)
        for j in range(len(openPos2)):
            nodes_expanded += 1
            min_move = openPos2[j]
            openPos3 = copy.deepcopy(openPos2)
            openPos3.remove(min_move)
            par_val2 = float("inf")
            for k in range(len(openPos3)):
                nodes_expanded += 1
                max_move_2 = openPos3[k]
                tboard = copy.deepcopy(board)
                tboard[max_move_1[0]][max_move_1[1]] = stones[player][0]
                tboard[min_move[0]][min_move[1]] = stones[opponent(player)][0]
                tboard[max_move_2[0]][max_move_2[1]] = stones[player][0]
                bval = evalboard(player,tboard)
                par_val2 = min([par_val2, bval])
                if par_val2 <= alpha:
                    break
                
            par_val = max([par_val, par_val2])
            if par_val >= beta:
                break
            alpha = max([alpha, par_val])
        if par_val > curr_best_val:
            curr_best_val = par_val
            curr_best_move = max_move_1
    nodes_expand[player].append(nodes_expanded)
    print('nodes expanded = ', nodes_expanded)
    return curr_best_move




def drawBoard(board):
    print('   |   |   |   |   |   |')
    print(' ' + board[6][0] + ' | ' + board[6][1] + ' | ' + board[6][2] + ' | ' + board[6][3] + ' | ' + board[6][4] + ' | ' + board[6][5] + ' | ' + board[6][6])
    print('   |   |   |   |   |   |')
    print('---------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + board[5][0] + ' | ' + board[5][1] + ' | ' + board[5][2] + ' | ' + board[5][3] + ' | ' + board[5][4] + ' | ' + board[5][5] + ' | ' + board[5][6])
    print('   |   |   |   |   |   |')
    print('---------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + board[4][0] + ' | ' + board[4][1] + ' | ' + board[4][2] + ' | ' + board[4][3] + ' | ' + board[4][4] + ' | ' + board[4][5] + ' | ' + board[4][6])
    print('   |   |   |   |   |   |')
    print('---------------------------')    
    print('   |   |   |   |   |   |')
    print(' ' + board[3][0] + ' | ' + board[3][1] + ' | ' + board[3][2] + ' | ' + board[3][3] + ' | ' + board[3][4] + ' | ' + board[3][5] + ' | ' + board[3][6])
    print('   |   |   |   |   |   |')
    print('---------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + board[2][0] + ' | ' + board[2][1] + ' | ' + board[2][2] + ' | ' + board[2][3] + ' | ' + board[2][4] + ' | ' + board[2][5] + ' | ' + board[2][6])
    print('   |   |   |   |   |   |')
    print('---------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + board[1][0] + ' | ' + board[1][1] + ' | ' + board[1][2] + ' | ' + board[1][3] + ' | ' + board[1][4] + ' | ' + board[1][5] + ' | ' + board[1][6])
    print('   |   |   |   |   |   |')
    print('---------------------------')
    print('   |   |   |   |   |   |')
    print(' ' + board[0][0] + ' | ' + board[0][1] + ' | ' + board[0][2] + ' | ' + board[0][3] + ' | ' + board[0][4] + ' | ' + board[0][5] + ' | ' + board[0][6])
    print('   |   |   |   |   |   |')

def whoGoesFirst():
    return 'player'
    # Randomly choose the player who goes first.
    #if random.randint(0, 1) == 0:
    #    return 'computer'
    #else:
    #    return 'player'

def isBoardFull(board):
    for i in range(0, 7):
        for j in range(0, 7):
            if isSpaceFree(board, i, j):
                return False
    return True

def makeMove(board, letter, x_loc, y_loc):
    board[x_loc][y_loc] = letter

def checkWin(board, player):
    for i in range (0, 7):
        for j in range(0, 3):
            state = ''
            for k in range (j, j+5):
                state += posState(board, i, k, player)
            if (state == '11111') :
                return True
            
    # vertical
    for i in range (0, 7):
        for j in range(0, 3):
            state = ''
            for k in range (j, j+5):
                state += posState(board, k, i, player)
            if (state == '11111') :
                return True
    # top-left diagonal - mid
    for i in range(0, 3):
        state = ''
        for j in range(i, i+5):
            state += posState(board, j, j, player)
        if (state == '11111') :
            return True
    # top-left diagonal - left
    for i in range(0, 2):
        state = ''
        for j in range(0,5):
            state += posState(board, j + i, j + 1 + i, player)
        if (state == '11111') :
            return True
    # top-left diagonal - right
    for i in range(0, 2):
        state = ''
        for j in range(0,5):
            state += posState(board, j + 1 + i, j + i, player)
        if (state == '11111') :
            return True

    for i in range(0, 1):
        state = ''
        for j in range(0, 5):
            state += posState(board, j, j + 2, player)
        if (state == '11111') :
            return True

    for i in range(0, 1):
        state = ''
        for j in range(0, 5):
            state += posState(board, j + 2, j, player)
        if (state == '11111') :
            return True

    # bottom-left diagonals
    for i in range(0, 3):
        state = ''
        for j in range(i, i+5):
            state += posState(board, 6-j, j, player)
        if (state == '11111') :
            return True
            
    for i in range(0, 2):
        state = ''
        for j in range(0,5):
            state += posState(board, 6-j-i, j+1+i, player)
        if (state == '11111') :
            return True
            
    for i in range(0, 2):
        state = ''
        for j in range(0,5):
            state += posState(board, 5-j-i, j+i, player)
        if (state == '11111') :
            return True
    return False


def isWinner_1(board):
    
    copy = getBoardCopy(board)

    for i in range(7):
        for j in range(7):
            if whos(copy, i, j) == 0 and whos(copy, i, j+1) == 0 and whos(copy, i, j+2) == 0 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 0:
                return True
            if whos(copy, i, j) == 0 and whos(copy, i+1, j) == 0 and whos(copy, i+2, j) == 0 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 0:
                return True
            if whos(copy, i, j) == 0 and whos(copy, i+1, j+1) == 0 and whos(copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 0:
                return True
            if whos(copy, i, j) == 0 and whos(copy, i+1, j-1) == 0 and whos(copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 0:
                return True
        
def isWinner_2(board):

    copy = getBoardCopy(board)

    for i in range(7):
        for j in range(7):
            if whos(copy, i, j) == 1 and whos(copy, i, j+1) == 1 and whos(copy, i, j+2) == 1 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 1:
                return True
            if whos(copy, i, j) == 1 and whos(copy, i+1, j) == 1 and whos(copy, i+2, j) == 1 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 1:
                return True
            if whos(copy, i, j) == 1 and whos(copy, i+1, j+1) == 1 and whos(copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 1:
                return True
            if whos(copy, i, j) == 1 and whos(copy, i+1, j-1) == 1 and whos(copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 1:
                return True

def getBoardCopy(board):
    # Make a duplicate of the board list and return it the duplicate.
    dupeBoard = []
    for i in board:
        dupeBoard.append(i)
    return dupeBoard

def isSpaceFree(board, x_loc, y_loc):
    return board[x_loc][y_loc] == ' '

def getPlayerMove(board):
    position_2 = input('x loc')
    position_1 = input('y loc')
    return (position_1, position_2)

def whos(board, x_loc, y_loc):
    computer = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    player = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if y_loc > 6:
        return -1
    if x_loc > 6:
        return -1
    #print('hi', x_loc, y_loc)
    for a in range(0,26):
        if board[x_loc][y_loc] == computer[a]:
            return 0
        elif board[x_loc][y_loc] == player[a]:
            return 1
        else:
            flag = 2
    #print('done')
    return flag

print('mp2')
computerLetter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
playerLetter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:
    # Reset the board
    theBoard = [[' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
    turn = whoGoesFirst()

    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            print('p1')
            # Player's turn.
            drawBoard(theBoard)
            move = minimax(theBoard,0)
            #print('where')
            c = int(move[0])
            d = int(move[1])
            makeMove(theBoard, playerLetter[0], c, d)
            print('where2')
            playerLetter.pop(0)
            if isWinner_2(theBoard):
                drawBoard(theBoard)
                print('p1 won')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('tie')
                    break
                else:
                    turn = 'computer'

        else:
            print('p2')
            # Computer's turn.
            move = alphabeta(theBoard, 1)
            a = int(move[0])
            b = int(move[1])
            makeMove(theBoard, computerLetter[0], a, b)
            computerLetter.pop(0)
            if isWinner_1(theBoard):
                drawBoard(theBoard)
                print('p2 won')
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('tie')
                    break
                else:
                    turn = 'player'
    break

'''
only for node calculation for minimax vs alphabeta
'''
'''
print("nodes expanded: ")
print("  Player 1  Player 2")
max_length = max([len(nodes_expand[0]), len(nodes_expand[1])])
for i in range(max_length):
    print(i,end="   ")
    if i >= len(nodes_expand[0]):
        print(0,end="   ")
    else:
        print(nodes_expand[0][i],end="   ")

    if i >= len(nodes_expand[1]):
        print(0,end="   ")
        print('\n')

    else:
        print(nodes_expand[1][i],end="   ")
        print('\n')
'''