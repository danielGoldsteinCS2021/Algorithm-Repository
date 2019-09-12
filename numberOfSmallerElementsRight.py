########################
# Daniel Goldstein
# number of smaller elements to the right
# August 13th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given an array of integers,
return a new array where each element
in the new array is the number of
smaller elements to the right of
that element in the original
input array.

For example, given the array [3, 4, 9, 6, 1],
return [1, 1, 2, 1, 0], since:

-There is 1 smaller element to the right of 3
-There is 1 smaller element to the right of 4
-There are two smaller elements to the right of 9
-There is 1 smaller element to the right of 6
-There are no smaller elements to the right of 1
'''

def findNumberOfSmaller(ls):
    lenLs = len(ls)
    rslt = [0 for i in range(lenLs)]
    for i in range(lenLs-1):
        for j in range(i+1, lenLs):
            if ls[i] > ls[j]:
                rslt[i] += 1
    return rslt

# TESTING
arr =  [3, 4, 9, 6, 1]
print("Testing with arr: ", arr, "\nResult is: ", findNumberOfSmaller(arr))
