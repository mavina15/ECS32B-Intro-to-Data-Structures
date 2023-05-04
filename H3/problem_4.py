'''
File Name: problem_4.py
Description: complete and test linked and array stacks
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
        return self.append(item)

    def pop(self): # Removes and returns the item at the top of the stack
        # Checks precondition
        oldItem = self.items[len(self)-1]
        self.size = -1
        # Resizes array
        return oldItem

def bracketsBalance(input_str,opening_list,closing_list):
    # Defaults is Balanced to true
    isBalanced = True

    # Creates stack from input string
    stack = []

    # For loop to iterate over each element in the stack
    for i in input_str:
        if i in opening_list:
            stack.append(i)
        elif i in closing_list:
            # Checks if stack is empty and if last element is equal to first element
            if not stack or opening_list[closing_list.index(i)] != stack.pop():
                return not isBalanced
    return isBalanced


if __name__ == "__main__":
    my_str = "([{))}"
    opening_list=['(', '[', '{']
    closing_list=[')', ')', '}']
    print(bracketsBalance(my_str,opening_list,closing_list)) # Correct Output: False

