"""
    Given a Linked List of size N, where every node represents a linked list
    and contains two pointers of its type:
    (i) a next pointer to the next node,
    (ii) a bottom pointer to a linked list where this node is head.

    You have to flatten the linked list to a single linked list which should be
    sorted.
    Note: The flattened list will be printed using the bottom pointer instead
    of next pointer.

    Your Task:
    This is a function problem. You need to complete the function flatten()
    that takes head of the list as parameter and returns the root of flattened
    list. The printing is done by the driver code.
"""
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

def helper(head1, head2):
    result = Node(-1)
    tail = result
    curr1 = head1
    curr2 = head2
    
    while curr1 and curr2:
        if curr1.data <= curr2.data:
            tail.bottom = curr1
            tail = curr1
            curr1 = curr1.bottom
        else:
            tail.bottom = curr2
            tail = curr2
            curr2 = curr2.bottom
    
    while curr1:
        tail.bottom = curr1
        tail = curr1
        curr1 = curr1.bottom
    
    while curr2:
        tail.bottom = curr2
        tail = curr2
        curr2 = curr2.bottom
        
    return result.bottom
    
    
def flatten(root):
    if not root:
       return None
       
    if not root.next:
        return root
      
    result = root
    curr = root.next
    
    while curr:
        result = helper(result, curr)
        curr = curr.next
    
    return result