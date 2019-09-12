########################
# Daniel Goldstein
# intersecting nodes problem
# July 22nd 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''

class Node:
    def __init__(self, val, nxt=None):
        self.value = val
        self.next = nxt

def intersectingNodes(linkLs1, linkLs2):
    node1, node2 = linkLs1, linkLs2
    c1, c2 = 0, 0 # -> count of number of elements
    while(node1 != None or node2 != None):
        if node1 != None:
            c1+=1
            node1 = node1.next
        if node2 != None:
            c2+=1
            node2 = node2.next
    cDiff = abs(c1-c2) # -> size difference
    node1, node2 = linkLs1, linkLs2
    while (node1 != None and node2 != None and node1.value != node2.value):
        if cDiff == 0: # -> once the lists have the same number of remaining elements
            node1 = node1.next
            node2 = node2.next
        elif c1>c2:
            node1 = node1.next
            cDiff-=1
        else:
            node2 = node2.next
            cDiff-=1
    return node1

# TESTING
def nodeToLs(node):
    temp = []
    while(node != None):
        temp.append(node.value)
        node = node.next
    return temp

linkLs1 = Node(3, Node(7, Node(8, Node(10))))
linkLs_1 = Node(99, Node(1, Node(8, Node(10)))) # - > 8
linkLs2 = Node(8)
linkLs_2 = Node(6) # - > None
linkLs3 = Node(1, Node(2, Node(3)))
linkLs_3 = Node(4, Node(5, Node(6))) # -> None
linkLs4 = Node(1, Node(2, Node(3)))
linkLs_4 = Node(4) # -> None
linkLs5 = Node(7)
linkLs_5 = Node(7) # -> 7
linkLs6 = Node(1, Node(2, Node(3, Node(4))))
linkLs_6 = Node(7, Node(3, Node(4))) # -> 3
linkLs7 = Node(7, Node(8, Node(9, Node(10))))
linkLs_7 = Node(2, Node(3, Node(4, Node(5, Node(12, Node(8, Node(9, Node(10)))))))) # -> 8

print("Testing with linkLs: ", nodeToLs(linkLs1), " and ", nodeToLs(linkLs_1), "\nResult is Node value: ", intersectingNodes(linkLs1, linkLs_1).value)
print("Testing with linkLs: ", nodeToLs(linkLs2), " and ", nodeToLs(linkLs_2), "\nResult is Node value: ", intersectingNodes(linkLs2, linkLs_2))
print("Testing with linkLs: ", nodeToLs(linkLs3), " and ", nodeToLs(linkLs_3), "\nResult is Node value: ", intersectingNodes(linkLs3, linkLs_3))
print("Testing with linkLs: ", nodeToLs(linkLs4), " and ", nodeToLs(linkLs_4), "\nResult is Node value: ", intersectingNodes(linkLs4, linkLs_4))
print("Testing with linkLs: ", nodeToLs(linkLs5), " and ", nodeToLs(linkLs_5), "\nResult is Node value: ", intersectingNodes(linkLs5, linkLs_5).value)
print("Testing with linkLs: ", nodeToLs(linkLs6), " and ", nodeToLs(linkLs_6), "\nResult is Node value: ", intersectingNodes(linkLs6, linkLs_6).value)
print("Testing with linkLs: ", nodeToLs(linkLs7), " and ", nodeToLs(linkLs_7), "\nResult is Node value: ", intersectingNodes(linkLs7, linkLs_7).value)
