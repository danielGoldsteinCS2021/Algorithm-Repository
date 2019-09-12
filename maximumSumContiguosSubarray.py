########################
# Daniel Goldstein
# maximum sum of contiguos subarrays
# July 23rd 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86],
the maximum sum would be 137, since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.

Do this in O(N) time.
'''

def maxSubArraySum(ls):
    maxSum, tempSum, lenLs = 0, 0, len(ls)
    for i in range(lenLs):
        if tempSum + ls[i] <= 0:
            tempSum = 0
        else:
            tempSum = tempSum+ls[i]
        if tempSum > maxSum:
            maxSum = tempSum
    return maxSum

# TESTING
a1 = [34, -50, 42, 14, -5, 86] # -> 137
a2 = [30] # -> 30
a3 = [-3] # -> 0
a4 = [88, -5, -6] # -> 88
a5 = [-6, 8, -2] # -> 8
a6 = [1, 2, 3, 4, -3, 22, 43, -8, 99, 1] # -> 164
a7 = [10, 87, -100, 88] # -> 97
a8 = [10, 90, -300, 121, -200, 30, 40, 10] # -> 121
a9 = [-2 ,-3, 4, -1, -2, 1, 5, -3] # -> 7

print("Testing with a1: ", a1, " max subarray value is: ", maxSubArraySum(a1))
print("Testing with a2: ", a2, " max subarray value is: ", maxSubArraySum(a2))
print("Testing with a3: ", a3, " max subarray value is: ", maxSubArraySum(a3))
print("Testing with a4: ", a4, " max subarray value is: ", maxSubArraySum(a4))
print("Testing with a5: ", a5, " max subarray value is: ", maxSubArraySum(a5))
print("Testing with a6: ", a6, " max subarray value is: ", maxSubArraySum(a6))
print("Testing with a7: ", a7, " max subarray value is: ", maxSubArraySum(a7))
print("Testing with a8: ", a8, " max subarray value is: ", maxSubArraySum(a8))
print("Testing with a9: ", a9, " max subarray value is: ", maxSubArraySum(a9))
