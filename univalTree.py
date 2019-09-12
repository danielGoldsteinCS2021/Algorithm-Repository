########################
# Daniel Goldstein
# unival tree problem
# June 17th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################
'''
A unival tree (which stands for "universal value")
is a tree where all nodes under it have the same value.
Given the root to a binary tree, count the number of unival subtrees.
For example, the following tree has 5 unival subtrees:

  0
 / \
1   0
   / \
  1   0
 / \
1   1

'''

class Node:
    def __init__(self, val, l=None, r=None):
        self.value = val
        self.left = l
        self.right = r

def univalTreeNumHelper(node, temp):
    if node == None:
        return 1 # -> empty tree
    left=univalTreeNumHelper(node.left, temp)
    right=univalTreeNumHelper(node.right, temp)
    if node.left == None and node.right == None: # -> leaf
        temp[0]+=1
        return 1
    elif right == 1 and left == 1 and node.left == None and node.value == node.right.value: # -> right only
        temp[0]+=1
        return 1
    elif right == 1 and left == 1 and node.right == None and node.left.value == node.value: # -> left only
        temp[0]+=1
        return 1
    elif node.left == None or node.right == None: # -> value != right or left
        return 0
    elif right == 1 and left == 1 and node.value == node.left.value and node.value == node.right.value: # -> left=right=value
        temp[0]+=1
        return 1
    else:
        return 0

def univalTreeNum(node):
    temp = [0]
    univalTreeNumHelper(node, temp)
    return temp[0]

# TESTING
t1 = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) # -> 5
t2 = Node(0) # -> 1
t3 = None # -> 0
t4 = Node(0, Node(0), Node(0, Node(0, Node(0, Node(0))), Node(0))) # -> 7
t5 = Node(1, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0))) # -> 5
t6 = Node(0, Node(1, Node(1)), Node(0, Node(1, Node(1, Node(1, Node(1)))), Node(0))) # -> 7
t7 = Node(0, Node(1, r=Node(1)), Node(0, Node(1, Node(1, Node(1))), Node(1))) # -> 6
t8 = Node(0, Node(1, r=Node(0)), Node(0, Node(1, r=Node(0, r=Node(1))), Node(0))) # -> 3
t9 = Node(0, Node(1), Node(0, Node(0, Node(0, Node(1))), Node(0))) # -> 3
t10 = Node(0, Node(1, Node(1, Node(1))), Node(0, Node(1, Node(1, Node(1))), Node(0))) # -> 7
t11 = Node(0, r=Node(0, Node(1, Node(1), Node(1)), Node(0))) # -> 4
t12 = Node(0, Node(0, Node(0, Node(0), Node(0))), Node(0, Node(0, Node(0, Node(0, Node(0, Node(1)))), Node(0)))) # -> 6
megaTree = Node(0, l=Node(0, Node(0, Node(0)), Node(0, Node(1, Node(0, r=Node(1, Node(1))), Node(0)), Node(1, Node(1), Node(1))))
                ,r=Node(1, Node(1, Node(0), Node(0)), Node(1, Node(1, Node(0, r=Node(0, Node(0, r=Node(1))))), Node(0, r=Node(1, r=Node(1, r=Node(1))))))) # -> 14

print("Testing with t1 , unival number is: ", univalTreeNum(t1))
print("Testing with t2 , unival number is: ", univalTreeNum(t2))
print("Testing with t3 , unival number is: ", univalTreeNum(t3))
print("Testing with t4 , unival number is: ", univalTreeNum(t4))
print("Testing with t5 , unival number is: ", univalTreeNum(t5))
print("Testing with t6 , unival number is: ", univalTreeNum(t6))
print("Testing with t7 , unival number is: ", univalTreeNum(t7))
print("Testing with t8 , unival number is: ", univalTreeNum(t8))
print("Testing with t9 , unival number is: ", univalTreeNum(t9))
print("Testing with t10 , unival number is: ", univalTreeNum(t10))
print("Testing with t11 , unival number is: ", univalTreeNum(t11))
print("Testing with t12 , unival number is: ", univalTreeNum(t12))
print("Testing with megaTree , unival number is: ", univalTreeNum(megaTree))
