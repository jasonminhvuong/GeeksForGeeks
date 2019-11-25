"""
    Given an unsorted linked list of N nodes. The task is to remove duplicate
    elements from this unsorted Linked List. If all the nodes in the linked
    list are equal, then remove n-1 nodes.

    User Task:
    You have to complete the method removeDuplicates() which takes 1 argument:
    the head of the  linked list  .You should not read any input from
    stdin/console. Your function should return a pointer to a linked list with
    no duplicate element.
"""
'''
	Your task is to remove duplicates from given 
	unsorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: head of the list after removing the duplicates from the list.
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
    
    s = set()
    curr = head.next
    prev = head
    s.add(head.data)
    
    while curr:
        if curr.data in s:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
        else:
            s.add(curr.data)
            prev = curr
            curr = curr.next
    
    return head