"""
    Given a linked list of N nodes where nodes can contain values 0s, 1s and 2s
    only. The task is to segregate 0s, 1s and 2s linked list such that all
    zeros segregate to headside, 2s at the end of the linked list and 1s in the
    mid of 0s and 2s

    Your Task:
    The task is to complete the function segregate() which segregate the nodes
    in the linked list as asked in the problem statement. The printing is done
    automatically by the driver code.
"""
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def segregate(head):
    n0 = 0
    n1 = 0
    n2 = 0
    
    curr = head
    while curr:
        if curr.data == 0:
            n0 += 1
        elif curr.data == 1:
            n1 += 1
        else:
            n2 += 1
        
        curr = curr.next
    
    curr = head
    while curr:
        if n0 > 0:
            curr.data = 0
            n0 -=1
        elif n1 > 0:
            curr.data = 1
            n1 -= 1
        else:
            curr.data = 2
        
        curr = curr.next
    
    return head