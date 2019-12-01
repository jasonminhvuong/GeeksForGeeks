"""
    Implement a Queue using Linked List.

    Your Task:
    Since this is a function problem, you don't need to take inputs. Just
    complete the provided functions. The printing is done automatically by
    the driver code.
"""
# A linked list (LL) node 
# to store a queue entry 
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class MyQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Method to add an item to the queue
    def push(self, item): 
        if not self.head:
            self.head = Node(item)
            self.tail = self.head
            return
        
        self.tail.next = Node(item)
        self.tail = self.tail.next
    
    # Method to remove an item from queue
    def pop(self):
        if not self.head:
            return -1
        
        result = self.head
        self.head = result.next
        
        if not self.head:
            self.tail = None
        
        return result.data