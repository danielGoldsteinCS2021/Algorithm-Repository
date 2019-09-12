########################
# Daniel Goldstein
# number of matrix traversals
# July 29th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
There is an N by M matrix of zeroes. Given N and M, write a function to
count the number of ways of starting at the top-left corner and
getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2,
since there are two ways to get to the bottom-right:

   Right, then down
   Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def matrixTraversal(matrix, curPos=(0,0), visited=None):
    if visited == None:
        visited = []
    rowLen, colLen = len(matrix), len(matrix[0])
    posX, posY = curPos[0], curPos[1]
    visited = visited.copy()
    visited.append(curPos)
    x, y = 0, 0
    if curPos == (colLen-1, rowLen-1):
        return 1
    if (posX+1, posY) not in visited and posX+1 < colLen: # -> right
        x=matrixTraversal(matrix, (posX+1, posY), visited)
    if (posX, posY+1) not in visited and posY+1 < rowLen: # -> down
        y=matrixTraversal(matrix, (posX, posY+1), visited)
    return x+y


# TESTING
arr1 = [[0,0], [0,0]] # -> 2
arr2 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]] # -> 70
arr3 = [[0,0,0], [0,0,0]] # -> 3
arr4 = [[0,0], [0,0], [0,0]] # -> 3

print("Testing with matrix: ", arr1, "\nResult is: ", matrixTraversal(arr1))
print("Testing with matrix: ", arr2, "\nResult is: ", matrixTraversal(arr2))
print("Testing with matrix: ", arr3, "\nResult is: ", matrixTraversal(arr3))
print("Testing with matrix: ", arr4, "\nResult is: ", matrixTraversal(arr4))
