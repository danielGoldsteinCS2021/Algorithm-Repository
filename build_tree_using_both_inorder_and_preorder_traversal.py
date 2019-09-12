########################
# Daniel Goldstein
# in/pre order traversal building
# July 22nd 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given pre-order and in-order traversals of a binary tree,
write a function to reconstruct the tree.
For example, given the following preorder traversal:
[a, b, d, e, c, f, g]
And the following inorder traversal:
[d, b, e, a, f, c, g]
You should return the following tree:

   a
  / \
 b    c
/ \   / \
d  e f   g

'''

class Node:
    def __init__(self, val, l=None, r=None):
        self.value = val
        self.left = l
        self.right = r
    def preOrder(self, node=False, ls=None):
        if node == False:
            node = self
        if node!=None:
            ls.append(node.value)
            print(node.value, end=" ")
            self.preOrder(node.left, ls)
            self.preOrder(node.right, ls)
    def inOrder(self, node=False, ls=None):
        if node == False:
            node = self
        if node!=None:
            self.inOrder(node.left, ls)
            ls.append(node.value)
            print(node.value, end=" ")
            self.inOrder(node.right, ls)

def buildTreePreinOr(pre, inOr, node=None):
    if pre == []:
        return node
    node = Node(pre[0])
    indx = inOr.index(pre[0])
    pre = pre[1:]
    preLeft, preRight = [], []
    for i in pre:
        if i in inOr[:indx]:
            preLeft.append(i)
        else:
            preRight.append(i)
    node.left = buildTreePreinOr(preLeft, inOr[:indx])
    node.right = buildTreePreinOr(preRight, inOr[indx+1:])
    return node


# TESTING
t1 = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f'), Node('g')))

print("Testing with t1")
print("Pre: ", end="")
lsPre=[]
t1.preOrder(ls=lsPre)
print()
print("In:  ", end="")
lsPost=[]
t1.inOrder(ls=lsPost)
print()
print("Building tree and printing In and Pre Order traversal of new tree:")
temp = buildTreePreinOr(lsPre, lsPost)
print("Pre: ", end="")
temp.preOrder(ls=[])
print()
print("In:  ", end="")
temp.inOrder(ls=[])
print()
