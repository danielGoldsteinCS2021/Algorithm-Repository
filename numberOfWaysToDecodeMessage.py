########################
# Daniel Goldstein
# number of ways to decode a message
# July 24th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given the mapping a = 1, b = 2, ... z = 26,
and an encoded message, count the number
of ways it can be decoded.
For example, the message '111' would give 3,
since it could be decoded as 'aaa', 'ka', and 'ak'.
You can assume that the messages are decodable.
For example, '001' is not allowed.
'''

def numberOfDecode(msg):
    if len(msg) == 1 or len(msg) == 0:
        return 1
    if (msg[0] == '1' or msg[0] == '2') and (msg[1] >= '1' and msg[1] <= '6'):
        return numberOfDecode(msg[1:])+numberOfDecode(msg[2:])
    return numberOfDecode(msg[1:])

# TESTING
print("Testing with 111: ", numberOfDecode('111'))
print("Testing with 11: ", numberOfDecode('11'))
print("Testing with 1: ", numberOfDecode('1'))
print("Testing with 123: ", numberOfDecode('123'))
print("Testing with 1111: ", numberOfDecode('1111'))
