'''
File Name: problem_1.py
Description: program uses stack to test strings for palindrome
Author: Mel Avina-Beltran
Date: 5/2/23
'''

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


def palindrome(input_str):
    # Defaults to false
    isPalindrome = False
    # Checks for if reverse of string is equal to string
    if  input_str == input_str[::-1]:
        return True
    else:
        return isPalindrome


if __name__ == "__main__":
    my_str = "noon"
    print(palindrome(my_str)) # Correct Ouput: True
