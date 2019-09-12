########################
# Daniel Goldstein
# remove Kth element from linked list
# July 24th 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Given a singly linked list and an integer k,
remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.
The list is very long, so making more than one pass is prohibitively expensive.
Do this in constant space and in one pass.
'''

class Node:
    def __init__(self, val, nxt=None):
        self.value = val
        self.next = nxt
    def printNode(self, node=None):
        if node == None:
            node = self
        while node!=None:
            print(node.value, end=" ")
            node=node.next

class LinkList:
    def __init__(self, head):
        self.head = head

def removeKthElement(linkLs, k):
    node = linkLs.head
    if k == 0: # -> remove first element
        linkLs.head = node.next
        return
    while (k!=1):
        k-=1
        node = node.next
    if node.next.next == None: # -> last element being removed
        node.next = None
    else:
        node.next = node.next.next # -> start < element to be removed < end
    return

# TESTING
l1 = LinkList(Node(1, Node(2, Node(3, Node(4, Node(5, Node(6)))))))
print("Testing with LinkList: ")
l1.head.printNode()
print("\nand k value 2 result is: ")
removeKthElement(l1, 2)
l1.head.printNode()
