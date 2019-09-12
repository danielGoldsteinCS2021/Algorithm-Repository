########################
# Daniel Goldstein
# numbers that add to k
# July 14th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given a list of numbers and a number k,
return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17,
return true since 10 + 7 is 17
'''

def addToK(ls, k):
    lenLs = len(ls)
    if lenLs < 2:
        return False
    temp = {} # dictionary, so runtime is O(n)
    for i in range(lenLs):
        if not(temp.get(ls[i])):
            temp[k - ls[i]] = 1
        else:
            return True
    return False

# TESTING
arr = [10, 15, 3, 7] # k 17, -> true
arr1 = [] # -> false
arr2 = [1] # -> false
arr3 = [10, 15] # k 25, true
arr4 = [1, 2, 3, 4, 5, 6] # k 7, 10, 12, 8, 20, 2, 3, 4, 6 -> t,t,f,t,f,f,t,t,t

print("Testing with array ", arr, " and K value 17\nResult: ", addToK(arr, 17))
print("Testing with array ", arr1, " and K value 17\nResult: ", addToK(arr1, 17))
print("Testing with array ", arr2, " and K value 17\nResult: ", addToK(arr2, 17))
print("Testing with array ", arr3, " and K value 25\nResult: ", addToK(arr3, 25))
print("Testing with array ", arr4, " and K value 7\nResult: ", addToK(arr4, 7))
print("Testing with array ", arr4, " and K value 10\nResult: ", addToK(arr4, 10))
print("Testing with array ", arr4, " and K value 12\nResult: ", addToK(arr4, 12))
print("Testing with array ", arr4, " and K value 8\nResult: ", addToK(arr4, 8))
print("Testing with array ", arr4, " and K value 20\nResult: ", addToK(arr4, 20))
print("Testing with array ", arr4, " and K value 2\nResult: ", addToK(arr4, 2))
print("Testing with array ", arr4, " and K value 3\nResult: ", addToK(arr4, 3))
print("Testing with array ", arr4, " and K value 4\nResult: ", addToK(arr4, 4))
print("Testing with array ", arr4, " and K value 6\nResult: ", addToK(arr4, 6))
