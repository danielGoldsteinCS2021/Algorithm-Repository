########################
# Daniel Goldstein
# staircase problem
# August 1 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
There exists a staircase with N steps, and you can climb up either 1 or 2
steps at a time. Given N, write a function that returns the number
of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

   1, 1, 1, 1
   2, 1, 1
   1, 2, 1
   1, 1, 2
   2, 2

What if, instead of being able to climb 1 or 2 steps at a time,
you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

def numOfWaysToClimb(n):
    if n <= 1:
        return 1
    return numOfWaysToClimb(n-1)+numOfWaysToClimb(n-2)

print("Tesiting with n = 1: ", numOfWaysToClimb(1)) # -> 1
print("Tesiting with n = 2: ", numOfWaysToClimb(2)) # -> 2
print("Tesiting with n = 3: ", numOfWaysToClimb(3)) # -> 3
print("Tesiting with n = 4: ", numOfWaysToClimb(4)) # -> 5
print("Tesiting with n = 5: ", numOfWaysToClimb(5)) # -> 8
print("Tesiting with n = 6: ", numOfWaysToClimb(6)) # -> 13

def numOfWaysToClimbSetOfSteps(n, ls):
    if n == 1:
        return 1
    if n == 0:
        return 0
    sum = 0
    for i in ls:
        if n-i > 0:
            sum += numOfWaysToClimbSetOfSteps(n-i, ls)
    return sum

print("Tesiting with n = 5, ls = [1, 2, 3]: ", numOfWaysToClimbSetOfSteps(5, [1,2,3])) # -> 7
