'''
File Name: problem_5.py
Description: add printing jobs to queue
Author: Mel Avina-Beltran
Date: 5/2/23
'''

# HW3 P5
# Please don't change any function names
# Node implementation provided! Don't touch it.

class Node:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None # The head of your list, don't change its name. It should be "None" when the list is empty.
        self.length = 0
        self.tail = None

    def __len__(self):
        return self.length
    
    def __str__(self):
        values = []
        node = self.head
        while node is not None and len(values) < 2 * self.length:
            values.append(node.val)
            node = node.next
        return str(values)
    
    def append(self, num): # append num to the tail of the list
        # Add num to end of list
        new_node = Node(num)

        # If list empty, new nodes at head and tail
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        # Else add new node to current tail 
        else: 
            self.tail.next = new_node
            self.tail = new_node
        
        # Update length of list
        self.length += 1

    def insert(self, index, num): # insert num into the given index
        new_node = Node(num)

        # If list is empty, head and tail are set to new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return
        
        # If index 0, node added to head
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
            return
        
        # Crosses list to node before being added
        current_node = self.head
        for i in range(index - 1):
            current_node = current_node.next

        # Adds node using current node pointer
        new_node.next = current_node.next
        current_node.next = new_node

        # If new node added to end, tail updates
        if new_node.next is None:
            self.tail = new_node
        
        # Update length of list
        self.length += 1

    def delete(self, index): # remove the node at the given index and return the deleted value as an integer
        part = None

        # If index 0, remove head
        if index == 0:
            part = self.head.val
            self.head = self.head.next
        else: 
            current_node = self.head
            for i in range(index - 1):
                current_node = current_node.next
            
            # Skips node and gets rid of it
            del_node = current_node.next
            part = del_node.val
            current_node.next = del_node.next
        
        # Length updates and returns deleted value
        self.length -= 1
        return part

    def circularize(self): # Make your list circular. This method can only be the last call of the autograder.
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = self.head
    


if __name__ == "__main__":
    list = LinkedList() # []
