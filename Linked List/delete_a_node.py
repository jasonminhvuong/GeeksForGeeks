"""
    Delete xth node from a singly linked list. Your task is to complete the
    method deleteNode() which takes two arguments: the address of the head of
    the linked list and an integer x. The function returns the head of the
    modified linked list.

    User Task:
    The task is to complete the function deleteNode() which should delete the
    node at required position.
"""

class node:
    def __init__(self):
        self.data = None
        self.next = None

def delNode(head, k):
    if not head:
        return None
    
    if k == 1:
        temp = head.next
        head.next = None
        return temp
    
    prev = head
    curr = head.next
    count = 2
    
    while curr:
        if count == k:
            prev.next = curr.next
            curr.next = None
            return head
        
        prev = curr
        curr = curr.next
        count += 1
        
    return head