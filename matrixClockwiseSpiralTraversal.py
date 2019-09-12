########################
# Daniel Goldstein
# matrix spiral
# August 2nd 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

[[1,  2,  3,  4,  5],
[6,  7,  8,  9,  10],
[11, 12, 13, 14, 15],
[16, 17, 18, 19, 20]]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12
'''
def spiralTraversal(m):
    rowLen, colLen = len(m), len(m[0])
    switchDir = False
    curRow, curCol = 0, -1
    for i in range(rowLen):
        for j in range(i, colLen):
            if switchDir == False:
                curCol += 1
                print(m[curRow][curCol])
            else:
                curCol -= 1
                print(m[curRow][curCol])
        for k in range(i+1, rowLen):
            if switchDir == False:
                curRow += 1
                print(m[curRow][curCol])
            else:
                curRow -= 1
                print(m[curRow][curCol])
        switchDir = not(switchDir)

def printMatrix(m):
    for i in m:
        for j in i:
            print(j, end=" ")
        print()
    print()

m = [[1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20]]
m1 = [[]]
m2= [[1, 2],
     [6, 7]]
m3 = [[1, 2]]
m4 = [[1]]
m5 = [[1, 2, 3, 4, 5, 6, 7],
      [24, 25, 26, 27, 28, 29, 8],
      [23, 40, 41, 42, 43, 30, 9],
      [22, 39, 48, 49, 44, 31, 10],
      [21, 38, 47, 46, 45, 32, 11],
      [20, 37, 36, 35, 34, 33, 12],
      [19, 18, 17, 16, 15, 14, 13]]

print("Testing with matrix: ")
printMatrix(m)
spiralTraversal(m)
print("Testing with matrix: ")
printMatrix(m1)
spiralTraversal(m1)
print("Testing with matrix: ")
printMatrix(m2)
spiralTraversal(m2)
print("Testing with matrix: ")
printMatrix(m3)
spiralTraversal(m3)
print("Testing with matrix: ")
printMatrix(m4)
spiralTraversal(m4)
print("Testing with matrix: ")
printMatrix(m5)
spiralTraversal(m5)
