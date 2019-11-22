"""
    You are given a pointer/ reference to the node which is to be deleted from
    the linked list of N nodes. The task is to delete the node. 
    Pointer/reference to head node is not given. 

    Note: No head reference is given to you.

    Your Task:
    This is a function problem. You only need to complete the function
    deleteNode that takes reference to the node that needs to be deleted. The
    printing is done automatically by the driver code.
"""
'''
    Your task is to delete the given node from
	the linked list, without using head pointer.
	
	Function Arguments: node (given node to be deleted) 
	Return Type: None, just delete the given node from the linked list.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def deleteNode(curr_node):
    if not curr_node:
        return
    
    if not curr_node.next:
        curr_node = None
    
    curr_node.data = curr_node.next.data
    curr_node.next = curr_node.next.next