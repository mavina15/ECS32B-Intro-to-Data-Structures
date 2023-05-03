'''
File Name: problem_3.py
Description:
Author: Mel Avina-Beltran
Date: 5/2/23
'''
#Reuse your Queue Implementation from Q2.
class Queue:

    def __init__(self, sourceCollection = None): # Constructor function
        self.sourceCollection = sourceCollection
        self.next = None

    def isEmpty(self): # Returns True if the queue is empty or False otherwise
        return len(self.items) == 0

    def __len__(self): # Returns the number of items in the stack
        return self.size

    def peek(self): # Returns the item at the front of the queue
        # Checks precondition
        return self.items[len(self)-1]

    def add(self, item): # Adds item to the rear of the queue
        self.items[len(self)] = item
        self.size += 1

    def pop(self): # Removes and returns the item at the front of the queue
        # Checks precondition
        oldItem = self.items[len(self)-1]
        self.size = -1
        # Resizes array
        return oldItem

    def remove(self, index): # Removes and returns the item at index of the queue
        return self.items.pop(index)


def stackToQueue(stack):
    q = Queue()
    while len(stack) > 0:
        q.add(stack.pop())
    return q

if __name__ == "__main__":
    stack = [1,2,3]
    res=stackToQueue(stack)
    print(res.pop()) #the autograder will use your Queue's pop() function, append to a list and compare with initial stack.
'''
Correct output of res would be a LinkedQueue in the order 3, 2, 1
'''
