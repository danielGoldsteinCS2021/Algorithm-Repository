########################
# Daniel Goldstein
# Alternating High Low LinkedList
# August 25th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given a linked list, rearrange the node values such
that they appear in alternating low -> high -> low -> high -> ... form
For example, given 1 -> 2 -> 3 -> 4 -> 5, you should return
1 -> 3 -> 2 -> 5 -> 4
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def printLinkList(n):
    while n != None:
        print(n.value, end=" ")
        n = n.next
    print()

def alternateList(node):
    head = node
    evenOdd = True
    while node.next != None:
        if ((node.value > node.next.value and evenOdd)
            or (node.value < node.next.value and not evenOdd)):
            node.value, node.next.value = node.next.value, node.value
        evenOdd = not(evenOdd)
        node = node.next
    return head

# TESTING
l1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print("Testing with: ")
printLinkList(l1)
print("Result is: ")
printLinkList(alternateList(l1)) # -> 13254

l2 = Node(1)
print("Testing with: ")
printLinkList(l2)
print("Result is: ")
printLinkList(alternateList(l2)) # -> 1

l3 = Node(1, Node(0, Node(2, Node(0, Node(3)))))
print("Testing with: ")
printLinkList(l3)
print("Result is: ")
printLinkList(alternateList(l3)) # -> 02031

l4 = Node(0, Node(1, Node(0, Node(1, Node(0)))))
print("Testing with: ")
printLinkList(l4)
print("Result is: ")
printLinkList(alternateList(l4)) # -> 01010

l5 = Node(1, Node(0))
print("Testing with: ")
printLinkList(l5)
print("Result is: ")
printLinkList(alternateList(l5)) # -> 01
