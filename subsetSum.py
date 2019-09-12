########################
# Daniel Goldstein
# Subset sum
# July 26th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given a list of integers S and a target number k,
write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list.
You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24,
return [12, 9, 2, 1] since it sums up to 24.

You can also return True and False
instead of the set itself.
'''


def subsetSum(ls, sum, lenLs=None):
    if lenLs == None:
        lenLs = len(ls)
    if lenLs == 0 and sum > 0:
        return False
    if sum == 0:
        return True
    if ls[lenLs-1] > sum:
        return subsetSum(ls, sum, lenLs-1)
    return subsetSum(ls, sum-ls[lenLs-1], lenLs-1) or subsetSum(ls, sum, lenLs-1)

# TESTING
arr1 = [12, 1, 61, 5, 9, 2] # -> sum=24 True, sum=1 True, k=700 False
arr2 = [] # -> False
arr3 = [2] # -> sum=2 True, sum=1 False


print("Testing with arr: ", arr1, "\nAnd sum 24:", subsetSum(arr1, 24))
print("Testing with arr: ", arr1, "\nAnd sum 1:", subsetSum(arr1, 1))
print("Testing with arr: ", arr1, "\nAnd sum 700:", subsetSum(arr1, 700))
print("Testing with arr: ", arr2, "\nAnd sum 0:", subsetSum(arr2, 0))
print("Testing with arr: ", arr2, "\nAnd sum 2:", subsetSum(arr2, 2))
print("Testing with arr: ", arr3, "\nAnd sum 2:", subsetSum(arr3, 2))
print("Testing with arr: ", arr3, "\nAnd sum 1:", subsetSum(arr3, 1))
