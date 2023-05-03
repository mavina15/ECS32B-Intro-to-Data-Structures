'''
File Name: problem_4.py
Description: 
Author: Mel Avina-Beltran
Date: 5/2/23
'''
#Reuse your Stack implementation from q1
from collections import deque

class Stack:

    def __init__(self, sourceCollection = None): # Constructor function
        self.sourceCollection = sourceCollection
        self.next = None

    def isEmpty(self): # Returns True if the stack is empty or False otherwise
        return len(self) == 0

    def __len__(self): # Returns the number of items in the stack
        return self.size

    def peek(self): # Returns the item at the top of the stack
        # Checks precondition
        return self.items[len(self)-1]

    def push(self, item): # Adds item to the top of the stack
        # Resizes array
        self.items[len(self)] = item
        self.size += 1

    def pop(self): # Removes and returns the item at the top of the stack
        # Checks precondition
        oldItem = self.items[len(self)-1]
        self.size = -1
        # Resizes array
        return oldItem

def bracketsBalance(input_str,opening_list,closing_list):
    if len(input_str) % 2 == 1:
        return False
    cheat_sheet = dict()
    for i in range(len(opening_list)):
        cheat_sheet[opening_list[i]] = closing_list[i]
    pos = 0
    isBalanced = True
    stk = Stack()

    #TODO: Your work here
    # Return if input_str is balanced or not
    return isBalanced

    if __name__ == "__main__":
        my_str = "([{))}"
        opening_list=['(', '[', '{']
        closing_list=[')', ')', '}']
        print(bracketsBalance(my_str,opening_list,closing_list)) # Correct Output:
        False
        #TODO (optional): Your testing code here
