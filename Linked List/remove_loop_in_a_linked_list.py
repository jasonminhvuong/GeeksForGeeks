"""
    You are given a linked list of N nodes. The task is to remove the loop
    from the linked list, if present.

    User Task:
    You don't have to read the input, or print the output. Just complete the
    function removeTheLoop() which has only argument as head reference of the
    linked list. If you complete this function in correct way and loop gets
    removed, the answer will be 1.
"""
#Structure of node
class Node:
    data=0
    next=None

def get_length_of_loop(slow, fast):
    count = 0
    
    while slow:
        count += 1
        slow = slow.next
        
        if slow == fast:
            break
    
    return count

def removeTheLoop(head):
    if not head or not head.next:
        return
    
    slow = head
    fast = head.next.next
    
    while fast:
        if slow == fast:
            break
        
        slow = slow.next
        fast = fast.next
        
        if not fast:
            return
        
        if slow == fast:
            break
        
        fast = fast.next
    
    if not fast:
        return
    
    count = get_length_of_loop(slow, fast)
    
    p1 = head
    p2 = head
    
    for _ in range(count):
        p2 = p2.next
    
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
        
    for _ in range(count-1):
        p2 = p2.next
    
    p2.next = None