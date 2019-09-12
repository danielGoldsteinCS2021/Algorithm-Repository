########################
# Daniel Goldstein
# two subset sum
# July 27th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given a multiset of integers, return whether it can be partitioned
into two subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10},
it would return true, since we can split it up into {15, 5, 10, 15, 10}
and {20, 35}, which both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, since
we can't split it up into two subsets that add up to the same sum.
'''

def twoSubsetSum(ls, n=None, sum1=0, sum2=None):
    if n == None:
        n = len(ls)
        sum2 = sum(ls)
    if ls == []:
        return False
    if sum1 == sum2:
        return True
    if n == 0:
        return False
    return (twoSubsetSum(ls, n-1, sum1+ls[n-1], sum2-ls[n-1])
            or twoSubsetSum(ls, n-1, sum1, sum2))

# TESTING
arr1 = [15, 5, 20, 10, 35, 15, 10] # -> True
arr2 = [] # -> False
arr3 = [1] # -> False
arr4 = [1, 1] # -> True
arr5 = [1, 2] # -> False
arr6 = [1, 2, 3] # -> True
arr7 = [1, 2, 4] # -> False
arr8 = [5, 3, 8, 1] # -> False
arr9 = [5, 6, 7, 87, 4, 3, 6, 7, 3, 4, 6, 3, 2, 4] # -> False
arr10 = [80, 80, 80, 80, 80, 80] # -> True
arr11 = [80, 80, 80, 80, 80] # -> False
arr12 = [2, 4, 5, 4, 3, 6, 53, 6, 5, 3, 56, 3, 3, 5, 3, 4, 4, 3, 4] # -> True
arr13 = [-1, -2, -3] # -> True
arr14 = [-1, -2, 3] # -> True, empty set + [-1, -2, 3]
arr15 = [-1, -2, 4] # -> False

print("Testing with arr1: ", arr1, "\nResult: ", twoSubsetSum(arr1))
print("Testing with arr2: ", arr2, "\nResult: ", twoSubsetSum(arr2))
print("Testing with arr3: ", arr3, "\nResult: ", twoSubsetSum(arr3))
print("Testing with arr4: ", arr4, "\nResult: ", twoSubsetSum(arr4))
print("Testing with arr5: ", arr5, "\nResult: ", twoSubsetSum(arr5))
print("Testing with arr6: ", arr6, "\nResult: ", twoSubsetSum(arr6))
print("Testing with arr7: ", arr7, "\nResult: ", twoSubsetSum(arr7))
print("Testing with arr8: ", arr8, "\nResult: ", twoSubsetSum(arr8))
print("Testing with arr9: ", arr9, "\nResult: ", twoSubsetSum(arr9))
print("Testing with arr10: ", arr10, "\nResult: ", twoSubsetSum(arr10))
print("Testing with arr11: ", arr11, "\nResult: ", twoSubsetSum(arr11))
print("Testing with arr12: ", arr12, "\nResult: ", twoSubsetSum(arr12))
print("Testing with arr13: ", arr13, "\nResult: ", twoSubsetSum(arr13))
print("Testing with arr14: ", arr14, "\nResult: ", twoSubsetSum(arr14))
print("Testing with arr15: ", arr15, "\nResult: ", twoSubsetSum(arr15))
