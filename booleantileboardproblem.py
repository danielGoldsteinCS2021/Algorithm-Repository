########################
# Daniel Goldstein
# boolean tile board problem
# June 6th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################
'''
Question:

You are given an M by N matrix consisting of
booleans that represents a board. Each True boolean
represents a wall. Each False boolean represents a tile you can walk on.

Given this matrix, a start coordinate,
and an end coordinate, return the minimum number of
steps required to reach the end coordinate from the start.
If there is no possible path, then return null. You can move up,
left, down, and right

example board:
[[0, 0, 0, 0],
[1, 1, 0, 1],
[0, 0, 0, 0],
[0, 0, 0, 0]]
If you start at the bottom left (3,0) it will take 7 moves to reach the
top left (0, 0)
'''

def boardSolver(board, currentPos, endPos, movLs):
    posY = currentPos[0]
    posX = currentPos[1]
    rowLen = len(board)
    colLen = len(board[0])
    z, y, x, k = None, None, None, None
    movLs = movLs.copy()
    movLs.append(currentPos)
    if currentPos == endPos:
        return 0
    # Right
    if (posX+1 < colLen
        and board[posY][posX+1] == 0
        and (posY, posX+1) not in movLs):
        x = boardSolver(board, (posY, posX+1), endPos, movLs)
    # left
    if (posX-1 >= 0
        and board[posY][posX-1] == 0
        and (posY, posX-1) not in movLs):
        y = boardSolver(board, (posY, posX-1), endPos, movLs)
    # Down
    if (posY+1 < rowLen
        and board[posY+1][posX] == 0
        and (posY+1, posX) not in movLs):
        z = boardSolver(board, (posY+1, posX), endPos, movLs)
    # Up
    if (posY-1 >= 0
        and board[posY-1][posX] == 0
        and (posY-1, posX) not in movLs):
        k = boardSolver(board, (posY-1, posX), endPos, movLs)
    temp = []
    for i in [x, y, z, k]:
        if i != None:
            temp.append(i)
    if temp!=[]:
        return 1+min(temp)
    return None


# TEST CASES #########################

x1 = [[0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]]

x2 = [[1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [0, 1, 1, 1]]

x3 = [[1, 0, 0, 0],
     [0, 1, 0, 1],
     [1, 0, 0, 1],
     [0, 0, 1, 0]]

x4 = [[1, 1, 0, 1],
     [1, 1, 0, 1],
     [1, 0, 0, 1],
     [1, 0, 1, 1]]

x5 = [[1, 0, 0, 0],
     [0, 1, 0, 0],
     [0, 0, 1, 0],
     [0, 0, 0, 1]]

x6 = [[1, 1, 1, 0],
     [0, 0, 0, 0],
     [0, 0, 1, 0],
     [1, 0, 0, 0]]

x7 = [[0, 0, 0, 1],
     [0, 0, 1, 1],
     [0, 1, 0, 1],
     [0, 0, 0, 1],
     [0, 0, 0, 1],
     [0, 1, 1, 1]]

x8 = [[0, 0, 1, 0, 0],
     [0, 1, 1, 0, 0],
     [0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0]]

x9 = [[1, 0, 0, 0],
     [1, 0, 1, 0],
     [1, 0, 0, 0],
     [1, 0, 1, 1]]


def printBoard(b):
    for i in b:
        print(i)

print("Board: (3,0) -> (0,0)")
printBoard(x1)
print("Number of moves: ", boardSolver(x1, (3,0), (0,0), []))

print("Board: (3,0) -> (0,0)")
printBoard(x2)
print("Number of moves: ", boardSolver(x2, (3,0), (0,0), []))

print("Board:  (3,0) -> (0,1)")
printBoard(x3)
print("Number of moves: ", boardSolver(x3, (3,0), (0,1), []))

print("Board: (3,1) -> (0,0)")
printBoard(x4)
print("Number of moves: ", boardSolver(x4, (3,1), (0,0), []))

print("Board: (3,0) -> (0,3)")
printBoard(x5)
print("Number of moves: ", boardSolver(x5, (3,0), (0,3), []))

print("Board: (3,1) -> (3,3)")
printBoard(x6)
print("Number of moves: ", boardSolver(x6, (3,1), (3,3), []))

print("Board: (5,0) -> (0,2)")
printBoard(x7)
print("Number of moves: ", boardSolver(x7, (5,0), (0,2), []))

print("Board: (3,0) -> (0,3)")
printBoard(x8)
print("Number of moves: ", boardSolver(x8, (3,0), (0,3), []))

print("Board: (3,1) -> (0,3)")
printBoard(x9)
print("Number of moves: ", boardSolver(x9, (3,1), (0,3), []))
