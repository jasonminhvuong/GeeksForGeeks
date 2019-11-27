"""
    Given a linked list of N nodes. The task is to check if the the linked list
    has a loop. Linked list can contain self loop.
    
    User Task:
    The task is to complete the function detectloop() which contains reference
    to the head as only argument. This function should return 1 if linked list
    contains loop, else return 0.
"""
'''
	Your task is to detect if any loop is present 
	in the given linked list.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: True or False (boolean)
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
	Contributed By: Nagendra Jha
'''
def detectLoop(head):
    if not head or not head.next:
        return False
        
    slow = head
    fast = head.next.next
    
    while fast:
        if slow == fast:
            return True
        
        fast = fast.next
        slow = slow.next
        
        if not fast:
            break
        
        if slow == fast:
            return True
        
        fast = fast.next
    
    return False