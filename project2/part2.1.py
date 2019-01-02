import random

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
    # Randomly choose the player who goes first.
    return 'player'
    '''
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    '''
def isBoardFull(board):
    for i in range(0, 7):
        for j in range(0, 7):
            if isSpaceFree(board, i, j):
                return False
    return True

def makeMove(board, letter, x_loc, y_loc):

    board[x_loc][y_loc] = letter

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

def getPlayerMove_1(board):
    position_2 = input('x loc')
    position_1 = input('y loc')
    return (position_1, position_2)

def getPlayerMove(board):


    copy = getBoardCopy(board)


    for i in range(0,7):
        for j in range(0,7):
            if whos(copy, i, j) == 1:
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
            x = 1
            y = 1
            return (x,y)

            #if whos(copy, x, y) == 2:
                #break



    if fl == 1:
        while True:
            for i in range(7):
                for j in range(7):
                    if whos(copy, i, j) == 1 and whos(copy, i, j+1) == 2 and whos(copy, i, j+2) == 1 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 1:
                        return(i, j+1)
                    if whos(copy, i, j) == 1 and whos(copy, i, j+1) == 1 and whos(copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 1:
                        return(i, j+2)
                    if whos(copy, i, j) == 1 and whos(copy, i, j+1) == 1 and whos(copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                        return(i, j+3)                   
                    if whos(copy, i, j) == 1 and whos(copy, i, j+1) == 1 and whos(copy, i, j+2) == 1 and whos(copy, i, j+3) == 1:
                        if whos(copy, i, j-1) == 2 and whos(copy, i, j+4) == 2 and j>=1:
                            return(i, j-1)
                        if whos(copy, i, j-1) == 2 and j>=1:
                            return(i, j-1)
                        if whos(copy, i, j+4) == 2:
                            return(i, j+4)

                    if whos(copy, i, j) == 1 and whos(copy, i+1, j) == 2 and whos(copy, i+2, j) == 1 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 1:
                        return(i+1, j)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j) == 1 and whos(copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 1:
                        return(i+2, j)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j) == 1 and whos(copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                        return(i+3, j)        
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j) == 1 and whos(copy, i+2, j) == 1 and whos(copy, i+3, j) == 1:
                        if whos(copy, i-1, j) == 2 and whos(copy, i+4, j) == 2 and i>=1:
                            return(i-1, j)
                        if whos(copy, i-1, j) == 2 and i>=1:
                            return(i-1, j)
                        if whos(copy, i+4, j) == 2:
                            return(i+4, j)

                    if whos(copy, i, j) == 1 and whos(copy, i+1, j+1) == 2 and whos(copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 1:
                        return(i+1, j+1)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j+1) == 1 and whos(copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 1:
                        return(i+2, j+2)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j+1) == 1 and whos(copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                        return(i+3, j+3)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j+1) == 1 and whos(copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1:
                        if whos(copy, i-1, j-1) == 2 and whos(copy, i+4, j+4) == 2 and j>=1 and i>=1:
                            return(i-1, j-1)
                        if whos(copy, i-1, j-1) == 2 and j>=1 and i>=1:
                            return(i-1, j-1)
                        if whos(copy, i+4, j+4) == 2:
                            return(i+4, j+4)

                    if whos(copy, i, j) == 1 and whos(copy, i+1, j-1) == 2 and whos(copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 1:
                        return(i+1, j-1)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j-1) == 1 and whos(copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 1:
                        return(i+2, j-2)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j-1) == 1 and whos(copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1:
                        return(i+3, j-3)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j-1) == 1 and whos(copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and j >= 4:
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
                    if whos(copy, i, j) == 0 and whos(copy, i, j+1) == 0 and whos(copy, i, j+2) == 0 and whos(copy, i, j+3) == 0:
                        if whos(copy, i, j-1) == 2 and j>=1:
                            return (i, j-1)
                        if whos(copy, i, j+4) == 2:
                            return (i, j+4)

                    #3 in a row vertical
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j) == 0 and whos(copy, i+2, j) == 0 and whos(copy, i+3, j) == 0:
                        if whos(copy, i-1, j) == 2 and i>=1:
                            return (i-1,j)
                        if whos(copy, i+4, j) == 2:
                            return (i+4,j)


                    #vertical 2
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j+1) == 0 and whos(copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0:
                        if whos(copy, i-1, j-1) == 2 and i>=1 and j>=1:
                            return (i-1,j-1)
                        if whos(copy, i+4, j+4) == 2:
                            return (i+4,j+4)



                    if whos(copy, i, j) == 0 and whos(copy, i+1, j-1) == 0 and whos(copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and j >= 4:
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
                    if whos(copy, i, j) == 0 and whos(copy, i, j+1) == 0 and whos(copy, i, j+2) == 0 and whos(copy, i, j-1) == 2 and whos(copy, i, j+3) == 2 and j>=1:
                        return (i,j-1)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j) == 0 and whos(copy, i+2, j) == 0 and whos(copy, i-1, j) == 2 and whos(copy, i+3, j) == 2 and i>=1:
                        return (i-1,j)

                    if whos(copy, i, j) == 0 and whos(copy, i+1, j+1) == 0 and whos(copy, i+2, j+2) == 0 and whos(copy, i-1, j-1) == 2 and whos(copy, i+3, j+3) == 2 and i>=1 and j>=1:
                        return (i-1,j-1)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j-1) == 0 and whos(copy, i+2, j-2) == 0 and whos(copy, i-1, j+1) == 2 and whos(copy, i+3, j-3) == 2 and  i>= 1:
                        return (i+3,j-3)

                    else:
                        fl = 4
            break


    if fl == 4:
        c = minimum_play_3(board)
        if c == (-1, -1):
                    #rule 4 dia1
                fl = 5
        else:
            return (c)

    if fl == 5:
        b = minimum_play_2(board)
        if b == (-1, -1):
                    #rule 4 dia1
                fl = 6
        else:
            return (b)



    if fl == 6:
        a = minimum_play_1(board)
        if a == (-1,-1):
            fl = 7
        else:
            return (a)

                    #rule 4 dia1



                    #rule 4 dia2



    if fl == 7:
        for a in range(7):
            for b in range(7):
                if whos(copy, a, b) == 2:
                    return(a,b)
    #return (x,y)
    '''

    
    position_2 = input('x loc')
    position_1 = input('y loc')

    return (position_1, position_2)
    '''
def whos(board, x_loc, y_loc):

    computer = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    player = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    empty = [' ']
    #print(x_loc, y_loc)
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
        elif board[x_loc][y_loc] == empty[0]:
            return 2
    #print('done')
    #return flag



def minimum_play_1(board):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                    v.append((i+3, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                    v.append((i, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                    v.append((i+3, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1 and j >= 5:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+1, j-1))
        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))
    #print(list3)

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)


def minimum_play_2(board):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 1:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))


                #rule 4 horizontal
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 1:
                    v.append((i, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))

                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))




                #rule 4 vertical
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 1:
                    v.append((i+2, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))

                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))


                #rule 4 dia2
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+4, j-4))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))



        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))
    #print(list3)

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)

def minimum_play_3(board):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 1:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+3, j+3))

                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 1:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 1:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j+1) == 1 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 1 and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))



                #rule 4 horizontal
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 1:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 1:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                    v.append((i, j+1))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 1:
                    v.append((i, j+2))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 1 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 1 and whos (copy, i, j+1) == 1 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 1 and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))


                #rule 4 vertical
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 1:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+3, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 1:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                    v.append((i+1, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 1:
                    v.append((i+2, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 1 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j) == 1 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 1 and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))


                #rule 4 dia2
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+4, j-4))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 1 and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 1 and whos (copy, i+1, j-1) == 1 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 1 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+2, j-2))

        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))
    #print(list3)

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)



def minimum_com_1(board):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                    v.append((i+3, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                    v.append((i, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                    v.append((i+3, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0 and j >= 5:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 5:
                    v.append((i+1, j-1))
        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))
    #print(list3)

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)
                    
def minimum_com_2(board):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 0:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))


                #rule 4 horizontal
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 0:
                    v.append((i, j+2))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))

                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))




                #rule 4 vertical
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 0:
                    v.append((i+2, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))

                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))


                #rule 4 dia2
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+4, j-4))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))


        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))
    #print(list3)

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)


def minimum_com_3(board):
    copy = getBoardCopy(board)
    v = []
    while True:
        for i in range(7):
            for j in range(7):
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 0:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 2:
                    v.append((i+3, j+3))

                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 0:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                    v.append((i+2, j+2))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 2 and whos (copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 2:
                    v.append((i+1, j+1))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j+1) == 0 and whos (copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 2:
                    v.append((i+2, j+2))



                #rule 4 horizontal
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 0:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 2:
                    v.append((i, j+3))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 0:
                    v.append((i, j+1))
                if whos(copy, i, j) == 2 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                    v.append((i, j+1))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                    v.append((i, j+2))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 2 and whos (copy, i, j+2) == 0 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 2:
                    v.append((i, j+1))
                if whos(copy, i, j) == 0 and whos (copy, i, j+1) == 0 and whos (copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 2:
                    v.append((i, j+2))


                #rule 4 vertical
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 0:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 2:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 2:
                    v.append((i+3, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 0:
                    v.append((i+1, j))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                    v.append((i+1, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                    v.append((i+2, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 2 and whos (copy, i+2, j) == 0 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 2:
                    v.append((i+1, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j) == 0 and whos (copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 2:
                    v.append((i+2, j))


                #rule 4 dia2
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+3, j-3))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+4, j-4))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 2 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i, j))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0 and j >= 4:
                    v.append((i+2, j-2))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 2 and whos (copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+1, j-1))
                if whos(copy, i, j) == 0 and whos (copy, i+1, j-1) == 0 and whos (copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 2 and j >= 4:
                    v.append((i+2, j-2))

        break

    list2 = sorted(v, key = lambda x: (x[1], x[0]))
    #list2 = list(zip(l,v))
    #list3 = sorted(list2, key = lambda x: (x[0][1], x[0][0]))
    #print(list3)

    if list2 == []:
        val = (-1, -1)
    else:
        val = list2[0]

    #res = l.index(min(l, key=lambda x: sum(x)))

    #val_2 = v[val]
    return (val)



def getComputerMove(board):

    comp_1 = 6
    comp_2 = 6
    copy = getBoardCopy(board)


    for i in range(0,7):
        for j in range(0,7):
            if whos(copy, i, j) == 0:
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
            x = 5
            y = 5
            return (x,y)
            #x = random.randint(0,6)
            #y = random.randint(0,6)
            
           # if whos(copy, x, y) == 2:
                #break



    if fl == 1:
        while True:
            for i in range(7):
                for j in range(7):

                    if whos(copy, i, j) == 0 and whos(copy, i, j+1) == 2 and whos(copy, i, j+2) == 0 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 0:
                        return(i, j+1)
                    if whos(copy, i, j) == 0 and whos(copy, i, j+1) == 0 and whos(copy, i, j+2) == 2 and whos(copy, i, j+3) == 0 and whos(copy, i, j+4) == 0:
                        return(i, j+2)
                    if whos(copy, i, j) == 0 and whos(copy, i, j+1) == 0 and whos(copy, i, j+2) == 0 and whos(copy, i, j+3) == 2 and whos(copy, i, j+4) == 0:
                        return(i, j+3)
                    if whos(copy, i, j) == 0 and whos(copy, i, j+1) == 0 and whos(copy, i, j+2) == 0 and whos(copy, i, j+3) == 0:
                        if whos(copy, i, j-1) == 2 and whos(copy, i, j+4) == 2 and j>=1:
                            return(i, j-1)
                        if whos(copy, i, j-1) == 2 and j>=1:
                            return(i, j-1)
                        if whos(copy, i, j+4) == 2:
                            return(i, j+4)


                    if whos(copy, i, j) == 0 and whos(copy, i+1, j) == 2 and whos(copy, i+2, j) == 0 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 0:
                        return(i+1, j)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j) == 0 and whos(copy, i+2, j) == 2 and whos(copy, i+3, j) == 0 and whos(copy, i+4, j) == 0:
                        return(i+2, j)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j) == 0 and whos(copy, i+2, j) == 0 and whos(copy, i+3, j) == 2 and whos(copy, i+4, j) == 0:
                        return(i+3, j) 
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j) == 0 and whos(copy, i+2, j) == 0 and whos(copy, i+3, j) == 0:
                        if whos(copy, i-1, j) == 2 and whos(copy, i+4, j) == 2 and i>=1:
                            return(i-1, j)
                        if whos(copy, i-1, j) == 2 and i>=1:
                            return(i-1, j)
                        if whos(copy, i+4, j) == 2:
                            return(i+4, j)

                    if whos(copy, i, j) == 0 and whos(copy, i+1, j+1) == 2 and whos(copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 0:
                        return(i+1, j+1)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j+1) == 0 and whos(copy, i+2, j+2) == 2 and whos(copy, i+3, j+3) == 0 and whos(copy, i+4, j+4) == 0:
                        return(i+2, j+2)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j+1) == 0 and whos(copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 2 and whos(copy, i+4, j+4) == 0:
                        return(i+3, j+3)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j+1) == 0 and whos(copy, i+2, j+2) == 0 and whos(copy, i+3, j+3) == 0:
                        if whos(copy, i-1, j-1) == 2 and whos(copy, i+4, j+4) == 2 and j>=1 and i>=1:
                            return(i-1, j-1)
                        if whos(copy, i-1, j-1) == 2 and j>=1 and i>=1:
                            return(i-1, j-1)
                        if whos(copy, i+4, j+4) == 2:
                            return(i+4, j+4)

                    if whos(copy, i, j) == 0 and whos(copy, i+1, j-1) == 2 and whos(copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 0:
                        return(i+1, j-1)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j-1) == 0 and whos(copy, i+2, j-2) == 2 and whos(copy, i+3, j-3) == 0 and whos(copy, i+4, j-4) == 0:
                        return(i+2, j-2)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j-1) == 0 and whos(copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 2 and whos(copy, i+4, j-4) == 0:
                        return(i+3, j-3)
                    if whos(copy, i, j) == 0 and whos(copy, i+1, j-1) == 0 and whos(copy, i+2, j-2) == 0 and whos(copy, i+3, j-3) == 0 and j >= 4:
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
                    if whos(copy, i, j) == 1 and whos(copy, i, j+1) == 1 and whos(copy, i, j+2) == 1 and whos(copy, i, j+3) == 1:
                        if whos(copy, i, j-1) == 2 and j>=1:
                            return (i, j-1)
                        if whos(copy, i, j+4) == 2:
                            return (i, j+4)

                        #4th one came up and j<=2?

                    #3 in a row vertical
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j) == 1 and whos(copy, i+2, j) == 1 and whos(copy, i+3, j) == 1:
                        #4th one came up and i<=2 ?
                        if whos(copy, i-1, j) == 2 and i>=1:
                            return (i-1,j)
                        if whos(copy, i+4, j) == 2:
                            return (i+4,j)

                    #vertical 2
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j+1) == 1 and whos(copy, i+2, j+2) == 1 and whos(copy, i+3, j+3) == 1:
                        if whos(copy, i-1, j-1) == 2 and i>=1 and j>=1:
                            return (i-1,j-1)
                        if whos(copy, i+4, j+4) == 2:
                            return (i+4,j+4)


                    if whos(copy, i, j) == 1 and whos(copy, i+1, j-1) == 1 and whos(copy, i+2, j-2) == 1 and whos(copy, i+3, j-3) == 1 and j >= 4:
                        if whos(copy, i-1, j+1) == 2 and i>=1:
                            return (i-1,j+1)
                        if whos(copy, i+4, j-4) == 2:
                            return (i+4,j-4)


                    else:
                        fl = 3
            break


    if fl == 3:
        print('B3')
        while True:
            for i in range(7):
                for j in range(7):
                    if whos(copy, i, j) == 1 and whos(copy, i, j+1) == 1 and whos(copy, i, j+2) == 1 and whos(copy, i, j-1) == 2 and whos(copy, i, j+3) == 2 and j>=1:
                        return (i,j-1)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j) == 1 and whos(copy, i+2, j) == 1 and whos(copy, i-1, j) == 2 and whos(copy, i+3, j) == 2 and i>=1:
                        return (i-1,j)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j+1) == 1 and whos(copy, i+2, j+2) == 1 and whos(copy, i-1, j-1) == 2 and whos(copy, i+3, j+3) == 2 and i>=1 and j>=1:
                        return (i-1,j-1)
                    if whos(copy, i, j) == 1 and whos(copy, i+1, j-1) == 1 and whos(copy, i+2, j-2) == 1 and whos(copy, i-1, j+1) == 2 and whos(copy, i+3, j-3) == 2 and  i>= 1:
                        return (i+3,j-3)
                    else:
                        fl = 4
            break


    if fl == 4:
        c = minimum_com_3(board)
        if c == (-1, -1):
                    #rule 4 dia1
                fl = 5
        else:
            return (c)

    if fl == 5:
        b = minimum_com_2(board)
        if b == (-1, -1):
                    #rule 4 dia1
                fl = 6
        else:
            return (b)

    if fl == 6:
        a = minimum_com_1(board)
        if a == (-1,-1):
            fl = 7
        else:
            return (a)


                    #rule 4 dia1



                    #rule 4 dia2



    if fl == 7:
        for a in range(7):
            for b in range(7):
                if whos(copy, a, b) == 2:
                    return(a,b)
    



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
            # Player's turn.
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            c = int(move[0])
            d = int(move[1])
            makeMove(theBoard, playerLetter[0], c, d)
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
            # Computer's turn.
            move = getComputerMove(theBoard)
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