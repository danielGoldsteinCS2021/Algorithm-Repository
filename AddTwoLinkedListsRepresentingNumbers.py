########################
# Daniel Goldstein
# Add two reversed linked lists
# August 07th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
We can represent an integer in a linked list format
by having each node represent a digit in the number.
The nodes are connected in reverse order, such that
the number 54321 is represented by the following linked list:
1->2->3->4->5
Given two linked lists in this format, return their sum
For example, given:
9->9
5->2
return 4->2->1, as 99+25 = 124
'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)

def printLinkList(n):
    while n != None:
        print(n.value, end=" ")
        n = n.next
    print()

def addLists(node1, node2):
    head, carry = Node(0), 0
    node = head
    while node1 != None or node2 != None:
        val1, val2 = 0, 0
        if node1 != None:
            val1 = node1.value
            node1 = node1.next
        if node2 != None:
            val2 = node2.value
            node2 = node2.next
        val3 = val1+val2+carry
        node.next = Node(val3%10)
        carry = val3//10
        node = node.next
    node.next = Node(carry) if carry > 0 else None
    return head.next

# TESTING
l1 = Node(9, Node(9, Node(6, Node(7, Node(8, Node(1))))))
l2 = Node(5, Node(2, Node(3)))
l3 = Node(9, Node(9))
l4 = Node(5, Node(2))

print("Testing with: ")
printLinkList(l1)
printLinkList(l2)
print("Result is: ")
printLinkList(addLists(l1, l2)) # -> 420881

print("Testing with: ")
printLinkList(l3)
printLinkList(l4)
print("Result is: ")
printLinkList(addLists(l3, l4)) # -> 421

print("Testing with: ")
printLinkList(l1)
printLinkList(l4)
print("Result is: ")
printLinkList(addLists(l1, l4)) # -> 427781

print("Testing with: ")
printLinkList(l2)
printLinkList(l4)
print("Result is: ")
printLinkList(addLists(l2, l4)) # -> 053

print("Testing with: ")
printLinkList(l3)
printLinkList(l2)
print("Result is: ")
printLinkList(addLists(l3, l2)) # -> 424
