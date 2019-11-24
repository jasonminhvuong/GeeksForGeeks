"""
    Given a linked list of size N. The task is to reverse every k nodes (where
    k is an input to the function) in the linked list.

    User Task:
    The task is to complete the function reverse() which should reverse the
    linked list in group of size k.
"""
def helper(head, k):
    curr = head
    prev = None
    tail = head
        
    for _ in range(k):
        if not curr:
            break
        
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    new_head = prev
    return new_head, tail, curr

def reverse(head, k):
    curr = head
    prev_tail = None
    result = None
    
    while curr:
        new_head, tail, curr = helper(curr, k)
        
        if not result:
            result = new_head
        
        if prev_tail:
            prev_tail.next = new_head
        
        prev_tail = tail
    
    return result