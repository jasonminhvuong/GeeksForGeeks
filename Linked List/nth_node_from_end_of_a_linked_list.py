"""
    Given a linked list consisting of L nodes and given a number N. The task is
    to find the Nth node from the end of the linked list.

    User Task:
    The task is to complete the function getNthFromLast() which takes two
    arguments: reference to head and N and you need to return Nth from end.
"""

'''
	Your task is to return the data stored in
	the nth end from end of linked list.
	
	Function Arguments: head (reference to head of the list), n (pos of node from end)
	Return Type: Integer or -1 if no such node exits.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def getNthfromEnd(head,n):
    if not head:
        return -1
    
    total = 0
    curr = head
    
    while curr:
        total += 1
        curr = curr.next
    
    dst_i = total - n
    
    curr = head
    while curr:
        if dst_i == 0:
            return curr.data
        dst_i -= 1
        curr = curr.next
    
    return -1