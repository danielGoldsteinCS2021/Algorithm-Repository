########################
# Daniel Goldstein
# binary tree arithmetic
# July 16th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.
Given the root to such a tree, write a function to evaluate it.
For example, given the following tree:
    *
   / \
 +     +
/ \   / \
3  2  4  5
You should return 45, as it is (3 + 2) * (4 + 5).
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.value = val
        self.left = left
        self.right = right
    def arithmeticExpression(self, node):
        if (self.left == None and self.right == None) or self.value == None:
            return 0 # -> empty tree
        if node.left == None and node.right == None:
            return node.value # -> leaf node
        left = self.arithmeticExpression(node.left)
        right = self.arithmeticExpression(node.right)
        if node.value == '+':
            return left + right
        elif node.value == '-':
            return left - right
        elif node.value == '*':
            return left * right
        else:
            return left / right
