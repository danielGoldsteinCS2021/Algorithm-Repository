########################
# Daniel Goldstein
# queue two stacks
# July 22nd 2019
# github: danielGoldsteinCS2021
# email: daniel.goldstein@queensu.ca
########################

'''
Implement a queue using two stacks.
Recall that a queue is a FIFO (first-in, first-out)
data structure with the following methods:
enqueue, which inserts an element into the queue, and dequeue, which removes it.
'''

class Stack:
    def __init__(self):
        self.stk = []
    def push(self, val):
        self.stk.append(val)
    def pop(self):
        return self.stk.pop()
    def peak(self):
        return self.stk[len(self.stk)-1]
    def isEmpty(self):
        return self.stk == []
    def __str__(self):
        return str(self.stk)

class Queue:
    def __init__(self):
        self.stk = Stack()
        self.__temp = Stack()
    def enqueue(self, val):
        while not(self.stk.isEmpty()):
            self.__temp.push(self.stk.pop())
        self.stk.push(val)
        while not(self.__temp.isEmpty()):
            self.stk.push(self.__temp.pop())
    def dequeue(self):
        self.stk.pop()
    def __str__(self):
        return str(self.stk)

# TESTING
print("Testing: ")
q = Queue()
print("Queue Status: ", q)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Enqueing: 1, 2, 3")
print("Queue Status: ", q)
q.dequeue()
print("Dequeing")
print("Queue Status: ", q)
q.enqueue(4)
print("Enqueing: 4")
print("Queue Status: ", q)
q.enqueue(5)
print("Enqueing: 5")
print("Queue Status: ", q)
print("Dequeing all")
q.dequeue()
print("Queue Status: ", q)
q.dequeue()
print("Queue Status: ", q)
q.dequeue()
print("Queue Status: ", q)
q.dequeue()
print("Queue Status: ", q)
q.enqueue(1)
print("Enqueing: 1")
print("Queue Status: ", q)
q.enqueue(2)
print("Enqueing: 2")
print("Queue Status: ", q)
q.enqueue(3)
print("Enqueing: 3")
print("Queue Status: ", q)
