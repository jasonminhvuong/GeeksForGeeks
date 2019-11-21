"""
    Given a singly linked list, your task is to remove every kth node from the
    linked list.

    User Task:
    The task is to complete the function deleteK() which should delete every
    kth nodes from the linked list.
"""

def deleteK(head, k):
    if not head or k == 1:
        return None
    
    prev = head
    curr = head.next
    count = 2
    del_i = k
    
    while curr:
        if del_i == count:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
            del_i += k
            count += 1
            continue
        
        prev = curr
        curr = curr.next
        count += 1
    
    return head