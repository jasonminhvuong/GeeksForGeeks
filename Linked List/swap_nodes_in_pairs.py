"""
    Given a singly linked list of size N. The task is to swap elements in the
    linked list pairwise.

    User Task:
    The task is to complete the function pairWiseSwap() which takes head node
    as the only argument and returns the modified head.
"""
def pairWiseSwap(head):
    curr = head
    
    while curr:
        prev = curr
        curr = curr.next
        
        if not curr:
            break
        
        temp = prev.data
        prev.data = curr.data
        curr.data = temp
        
        curr = curr.next
    
    return head