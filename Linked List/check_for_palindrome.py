"""
    Given a singly linked list of size N of integers. The task is to check if
    the given linked list is palindrome or not.

    User Task:
    The task is to complete the function isPalindrome() which takes head as
    reference as the only parameter and returns true or false if linked list is
    palindrome or not respectively.
"""

'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.
	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''
def helper(head):
    curr = head
    prev = None
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    return prev

def isPalindrome(head):
    n = 0
    curr = head
    
    while curr:
        n += 1
        curr = curr.next
    
    if n == 0 or n == 1:
        return True
    
    head2_i = n // 2
        
    if n % 2 == 1:
        head2_i += 1

    curr = head
    count = 0
    while curr:
        count += 1
        if count == head2_i:
            break
        
        curr = curr.next
    
    head2 = helper(curr)
    
    while head and head2:
        if head.data != head2.data:
            return False
        
        head = head.next
        head2 = head2.next
    
    return True