'''
File Name: problem_2.py
Description:
Author: Mel Avina-Beltran
Date: 5/2/23
'''

class Queue:

    def __init__(self, sourceCollection = None): # Constructor function
        self.sourceCollection = sourceCollection
        self.next = None

    def isEmpty(self): # Returns True if the queue is empty or False otherwise
        return len(self) == 0

    def __len__(self): # Returns the number of items in the stack
        return self.size

    def peek(self): # Returns the item at the front of the queue
        # Checks precondition
        return self.items[len(self)-1]

    def add(self, item): # Adds item to the rear of the queue
        self.items.append(item)

    def pop(self): # Removes and returns the item at the front of the queue
        # Checks precondition
        oldItem = self.items[len(self)-1]
        self.size = -1
        # Resizes array
        return oldItem

    def remove(self, index): # Removes and returns the item at index of the queue
        return self.items.pop(index)


if __name__ == "__main__":
    queue = Queue()
    q.add(1)
    q.add(3)
    q.add(5)
    q.add(7)
    print(q.pop())
    print(q.remove(1))
    print(q.pop())
