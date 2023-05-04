'''
File Name: problem_3.py
Description: function builds and returns instance of LinkedQueue with items in stack
Author: Mel Avina-Beltran
Date: 5/2/23
'''
#Reuse your Queue Implementation from Q2.

class Queue:

    def __init__(self): # Constructor function
        self.items = []

    def isEmpty(self): # Returns True if the queue is empty or False otherwise
        return len(self.items) == 0

    def len(self): # Returns the number of items in the stack
        return len(self.items)

    def peek(self): # Returns the item at the front of the queue
        if self.isEmpty():
            return None
        return self.items[0]

    def add(self, item): # Adds item to the rear of the queue
        self.items.append(item)

    def pop(self): # Removes and returns the item at the front of the queue
        if self.isEmpty():
            return None
        return self.items.pop(0)

    def remove(self, index): # Removes and returns the item at index of the queue
        return self.items.pop(index)

def stackToQueue(stack):
    # Creates queue
    Q = Queue()

    # While loop that checks that stack is not empty (ie. length of collection of data strucure/stack)
    while len(stack) > 0:
        Q.add(stack.pop())
    return Q

if __name__ == "__main__":
    stack = [1,2,3]
    res=stackToQueue(stack)
    # While loop that checks the length of the object (ie. res)
    while res.len() > 0:
        print(res.pop())

