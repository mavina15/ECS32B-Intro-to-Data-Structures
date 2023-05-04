'''
File Name: problem_2.py
Description: add printing jobs to queue
Author: Mel Avina-Beltran
Date: 5/2/23
'''

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


if __name__ == "__main__":
    # Creates queue
    Q = Queue()
