"""
    Let's give it a try! You have a linked list and you have to implement the
    functionalities push and pop of stack using this given linked list.

    Your Task:
    You are required to complete the two methods push() which take one argument
    an integer 'x' to be pushed into the stack  and pop() which returns a
    integer poped out from the stack.
"""

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        node = StackNode(data)
        
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node
    
    def pop(self):
        if not self.head:
            return -1
        
        node = self.head
        self.head = self.head.next
        node.next = None
        
        return node.data