"""
    Given a singly linked list of N nodes. The task is to find middle of the
    linked list. For example, if given linked list is 1->2->3->4->5 then output
    should be 3.
    If there are even nodes, then there would be two middle nodes, we need to
    print second middle element. For example, if given linked list is
    1->2->3->4->5->6 then output should be 4.

    User Task:
    The task is to complete the function getMiddle() which takes head reference
    as the only argument and should return the data at the middle node of
    linked list.
"""

def findMid(head):
    if not head:
        return -1
        
    fast = head
    slow = head
    
    while fast.next:
        fast = fast.next
        slow = slow.next
        
        if fast.next:
            fast = fast.next
        
    
    return slow