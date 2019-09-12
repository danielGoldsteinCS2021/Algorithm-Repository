########################
# Daniel Goldstein
# exponent function
# July 29th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Implement integer exponentiation.
That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
Do this faster than the naive method of repeated multiplication.
For example, pow(2, 10) should return 1024.
'''


def pow(b, p):
    if p == 0:
        return 1
    if p == 1:
        return b
    temp = pow(b, p//2) # allows for log(n) runtime
    if p%2 == 0:
        return temp*temp
    else:
        return temp*temp*b

# TESTING
print("Testing for 3, 0: ", pow(3,0))
print("Testing for 3, 1: ", pow(3,1))
print("Testing for 3, 2: ", pow(3,2))
print("Testing for 3, 3: ", pow(3,3))
print("Testing for 2, 4: ", pow(2,4))
print("Testing for 16, 3: ", pow(16,3))
