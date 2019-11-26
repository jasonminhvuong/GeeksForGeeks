"""
    Given a singly linked list, find if the linked list is circular or not. A
    linked list is called circular if it not NULL terminated and all nodes are
    connected in the form of a cycle. An empty linked list is considered as
    circular.

    User Task:
    The task is to complete the function isCircular() which checks if the given
    linked list is circular or not. It should return true or false accordingly.
"""
class Node:
   def __init__(self, data):
       self.data = data
       self.next = None

# your task is to complete this function
# function should return true/false or 1/0
def isCircular(head):
    if not head:
        return True
        
    curr = head.next
    
    while curr:
        if curr == head:
            return True
        
        curr = curr.next
    
    return False