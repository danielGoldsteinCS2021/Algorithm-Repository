########################
# Daniel Goldstein
# max value in stack
# July 15th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Implement a stack that has the following methods:
- push(val), which pushes an element onto the stack
- pop(), which pops off and returns the topmost element of the stack.
  If there are no elements in the stack, then it should throw an error or return null.
- max(), which returns the maximum value in the stack currently.
  If there are no elements in the stack, then it should throw an error or return null.

Each method should run in constant time.
'''

 # I build another stack along the main Stack
 # and I use this stack (maxStk) to track the max value
 # for each element in the stack
 # so I will always have a max value even when elements are popped
class Stack:
    def __init__(self):
        self.stk = []
        self.maxStk = []
        self.maxVal = None
        self.size = 0
    def push(self, val):
        self.size+=1
        if self.maxVal == None or self.maxVal < val:
            self.maxVal = val
        self.stk.append(val)
        self.maxStk.append(self.maxVal)
    def pop(self):
        self.size-=1
        x=self.stk[self.size]
        self.stk = self.stk[:self.size]
        self.maxStk = self.maxStk[:self.size]
        self.maxVal = self.maxStk[self.size-1]
        return x
    def max(self):
        return self.maxVal
