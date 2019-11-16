"""
    Given a singly linked list with N nodes and a number X. The task is to find
    the node at the given index (X)(1 based index) of linked list.

    User Task:
    The task is to complete the function GetNth() which takes head reference
    and index as arguments and should return the data at Xth position in the
    linked list.
"""

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
This is method only submission.
 You only need to complete below method.

def getNth(head, k):
    count = 0
    curr = head
    while curr:
        count += 1
        
        if count == k:
            return curr.data
            
        curr = curr.next
    
    return -1
