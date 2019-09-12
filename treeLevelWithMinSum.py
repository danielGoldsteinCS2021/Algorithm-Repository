########################
# Daniel Goldstein
# tree level with minimum sum
# August 20th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given a binary tree, return the level of the tree
that has the minimum sum. The level of a node is
defined as the number of connections required to get
to the root, with the root having level zero.
'''

from collections import deque, defaultdict

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.value)

def getTreeLevelMinSum(node):
    q, dic, level = deque(), defaultdict(int), 0
    q.append((node, level))
    while q:
        node, level = q.popleft()
        dic[level] += node.value
        if node.left:
            q.append((node.left, level+1))
        if node.right:
            q.append((node.right, level+1))
    return min(dic.values())


# TESTING
t1 = Node(1, Node(2), Node(3, Node(4), Node(5))) # -> 1
t2 = Node(100, Node(99, Node(99, Node(98, Node(97, Node(2)))))) # -> 2
t3 = Node(3) # -> 3

print("Testing with t1, result is: ", getTreeLevelMinSum(t1))
print("Testing with t2, result is: ", getTreeLevelMinSum(t2))
print("Testing with t3, result is: ", getTreeLevelMinSum(t3))
