########################
# Daniel Goldstein
# cut birck wall
# August 12th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
A wall consists of several rows of bricks of various
integer lengths and uniform height. Your goal is to find
a vertical line going from the top to the bottom of the wall
that cuts through the fewest number of bricks. If the line
goes through the edge between two bricks, this does not
count as a cut.

For example, suppose the input is as follows, where values
in each row represent the lengths of bricks in that row:
[[3, 5, 1, 1],
 [2, 3, 3, 2],
 [5, 5],
 [4, 4, 2],
 [1, 3, 3, 3],
 [1, 1, 6, 1, 1]]

The best we can do here is to draw
a line after the eighth brick, which will
only require cutting through the bricks in the
third and fifth row.

Given an input consisting of brick lengths
for each row such as the one above, return
the fewest number of bricks that must be cut
to create a vertical line.
'''

def cutBrickWall(wall):
    wallLen, cutTable = len(wall), {}
    totalBirckLen = sum(wall[0])
    for i in range(1, totalBirckLen+1): # -> to avoid key error
        cutTable[i] = 0
    for row in wall:
        brickLen = 0
        for brick in row:
            brickLen += brick
            cutTable[brickLen] += 1 # -> adding 1 clean cut at each edge
    cutTable[totalBirckLen] = 0 # -> makes it so we can't cut along end of wall,
                                # -> as we can avoid cutting any bricks doing so
    return wallLen - max(cutTable.values())

def printWall(w):
    for i in w:
        for j in i:
            print(j, end = " ")
        print()

# TESTING
w1 = [[3, 5, 1, 1],
      [2, 3, 3, 2],
      [5, 5],
      [4, 4, 2],
      [1, 3, 3, 3],
      [1, 1, 6, 1, 1]]

print("Testing with: ")
printWall(w1)
print("Result is: ", cutBrickWall(w1), " bricks")
