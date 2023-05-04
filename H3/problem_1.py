'''
File Name: problem_1.py
Description: program uses stack to test strings for palindrome
Author: Mel Avina-Beltran
Date: 5/2/23
'''

class Stack():

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
        #self.items[len(self)] = item
        #self.size += 1

    def pop(self): # Removes and returns the item at the top of the stack
        # Checks precondition
        oldItem = self.items[len(self)-1]
        self.size = -1
        # Resizes array
        return oldItem


def palindrome(input_str):
    # Defaults to false
    isPalindrome = False
    # Creates stack
    stack = []

    # Compares first and last elements of list 
    # Adds element to end of list 
    for s in input_str: 
        stack.append(s)
    
    # Returns and removes element on top of stack
    for s in input_str: 
        if s != stack.pop():
            return isPalindrome
    return not isPalindrome
        

if __name__ == "__main__":
    s = "noon"
    print(palindrome(s)) # Correct Ouput: True
