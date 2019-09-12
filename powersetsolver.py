########################
# Daniel Goldstein
# power set
# July 12th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.
'''


def zeroPaddingBinaryNum(n, padNum):
    temp = bin(n)[2:]
    rslt = []
    for i in range(padNum - len(temp)):
        rslt.append(0)
    for j in temp:
        rslt.append(int(j))
    return rslt

def powerSet(ls):
    rslt, temp = [], []
    padNum = len(ls)
    powerSetLen = 2**len(ls)
    for i in range(powerSetLen):
        n = zeroPaddingBinaryNum(i, padNum)
        nLen = len(n)
        for j in range(nLen):
            if n[j] == 1:
                temp.append(ls[j])
        rslt.append(temp)
        temp = []
    return rslt

# TESTING
x1 = []
x2 = [1]
x3 = [1,2]
x4 = [1,2,3]
x5 = [1,2,3,4]
x6 = [1,2,3,4,5]
x7 = [1,2,3,4,5,6]

print("Testing for: ", x1, "\n", powerSet(x1), "\nLength of set is: ", (len(powerSet(x1))))
print("Testing for: ", x2, "\n", powerSet(x2), "\nLength of set is: ", (len(powerSet(x2))))
print("Testing for: ", x3, "\n", powerSet(x3), "\nLength of set is: ", (len(powerSet(x3))))
print("Testing for: ", x4, "\n", powerSet(x4), "\nLength of set is: ", (len(powerSet(x4))))
print("Testing for: ", x5, "\n", powerSet(x5), "\nLength of set is: ", (len(powerSet(x5))))
print("Testing for: ", x6, "\n", powerSet(x6), "\nLength of set is: ", (len(powerSet(x6))))
print("Testing for: ", x7, "\n", powerSet(x7), "\nLength of set is: ", (len(powerSet(x7))))
