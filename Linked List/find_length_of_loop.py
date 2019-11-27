"""
    Given a linked list of size N. The task is to complete the function
    countNodesinLoop() that checks whether a given Linked List contains loop or
    not and if loop is present then return the count of nodes in loop or else
    return 0.

    User Task:
    The task is to complete the function countNodesinLoop() which contains the
    only argument as reference to head of linked list.
"""

#Structure of node
class Node:
    data=0
    next=None
    
    
def newNode(data):
    temp=Node()
    temp.data=data
    temp.next=None
    return temp

def countNodesinLoop(head):
    if not head or not head.next:
        return 0
    
    slow = head
    fast = head.next.next
    
    while fast:
        if slow == fast:
            break
        
        slow = slow.next
        fast = fast.next
        
        if not fast:
            return 0
        
        if slow == fast:
            break
        
        fast = fast.next
    
    if not fast:
        return 0
        
    count = 0
    
    while slow:
        slow = slow.next
        count += 1
        
        if slow == fast:
            return count