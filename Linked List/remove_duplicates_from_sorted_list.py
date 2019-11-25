"""
    Given a singly linked list consisting of N nodes. The task is to remove
    duplicates (nodes with duplicate values) from the given list (if exists).

    Note: Try not to use extra space. Expected time complexity is O(N). The
    nodes are arranged in a sorted way.

    User Task:
    The task is to complete the function removeDuplicates() which should remove
    the duplicates from linked list. The printing is done automatically by the
    driver code
"""
'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def removeDuplicates(head):
    if not head:
        return None
    
    curr = head.next
    prev = head
    
    while curr:
        if curr.data == prev.data:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
        else:
            prev = curr
            curr = curr.next
    
    return head