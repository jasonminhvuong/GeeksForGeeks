"""
    Given a linked list of N nodes. The task is to reverse this list.

    User Task:
    The task is to complete the function reverseList() which head reference as
    the only argument and should return new head after reversing the list.
"""
def reverseList(self):
    if self.head is None:
        return None
    
    curr = self.head
    prev = None
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
        
    self.head = prev