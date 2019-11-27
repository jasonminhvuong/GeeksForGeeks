"""
    Given two sorted linked lists consisting of N and M nodes respectively. The
    task is to merge both of the list (in-place) and return head of the merged
    list.
    Note: It is strongly recommended to do merging in-place using O(1) extra
    space.

    User Task:
    The task is to complete the function sortedMerge() which takes references
    to the heads of two linked lists as the arguments and returns the head of
    merged linked list.
"""
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def merge(head_a,head_b):
    if not head_a:
        return head_b
    elif not head_b:
        return head_a
        
    curr1 = head_a
    curr2 = head_b
    result = Node(-1)
    tail = result
    
    while curr1 and curr2:
        if curr1.data <= curr2.data:
            temp = curr1.next
            tail.next = curr1
            tail = curr1
            tail.next = None
            curr1 = temp
        else:
            temp = curr2.next
            tail.next = curr2
            tail = curr2
            tail.next = None
            curr2 = temp
        
    while curr1:
        temp = curr1.next
        tail.next = curr1
        tail = curr1
        tail.next = None
        curr1 = temp
    
    while curr2:
        temp = curr2.next
        tail.next = curr2
        tail = curr2
        tail.next = None
        curr2 = temp
    
    return result.next