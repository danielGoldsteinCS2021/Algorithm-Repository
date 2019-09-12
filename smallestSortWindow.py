########################
# Daniel Goldstein
# number of matrix traversals
# August 8th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given an array of integers that are out of order,
determine the bounds of the smallest window that must be sorted.
For example given [3, 7, 5, 6, 9], you should return (1, 3)
'''

def smallestWindow(arr):
    arrLen = len(arr)
    x, y = None, None
    if arrLen != 0:
        maxSoFar = arr[0]
        minSoFar = arr[arrLen-1]
    for i in range(arrLen):
        maxSoFar = max(maxSoFar, arr[i])
        if arr[i] < maxSoFar:
            x = i
    for j in range(arrLen-1, -1, -1):
        minSoFar = min(minSoFar, arr[j])
        if arr[j] > minSoFar:
            y = j
    return y, x

# TESTING
arr = [3, 7, 5, 6, 9]
arr1 = [1, 2, 3, 68, 67, 4, 46, 99, 1005]
arr2 = [55, 44, 23, 1]
arr3 = []
arr4 = [1]
arr5 = [1, 2]
arr6 = [2, 1]

print("Testing with array: ", arr, "\nResult: ", smallestWindow(arr))
print("Testing with array: ", arr1, "\nResult: ", smallestWindow(arr1))
print("Testing with array: ", arr2, "\nResult: ", smallestWindow(arr2))
print("Testing with array: ", arr3, "\nResult: ", smallestWindow(arr3))
print("Testing with array: ", arr4, "\nResult: ", smallestWindow(arr4))
print("Testing with array: ", arr5, "\nResult: ", smallestWindow(arr5))
print("Testing with array: ", arr6, "\nResult: ", smallestWindow(arr6))
