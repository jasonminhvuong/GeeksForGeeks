"""
    Given a linked list, delete N nodes after skipping M nodes of a linked list
    until the last of the linked list.

    User Task:
    The task is to complete the function skipMdeleteN() which should modify the
    linked list as required.
"""
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

def skipMdeleteN(head, M, N):
    curr = head
    
    while curr:
        for i in range(M-1):
            if not curr:
                return
            
            curr = curr.next
        
        if not curr:
            return
        
        t = curr.next
        for i in range(N):
            if not t:
                break
            
            t = t.next
        
        curr.next = t
        curr = t