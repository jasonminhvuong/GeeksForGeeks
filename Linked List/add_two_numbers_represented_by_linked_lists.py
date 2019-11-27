"""
    Given two numbers represented by two linked lists of size N and M. The task
    is to return a sum list. The sum list which is a linked list representation
    of addition of two input numbers.
    
    User Task:
    The task is to complete the function addTwoLists() which has node reference
    of both the linked lists and returns the head of new list.
"""
'''
	Function to add two numbers represented 
	in the form of the linked list.
	
	Function Arguments: head_a and head_b (heads of both the linked lists)
	Return Type: head of the resultant linked list.
    
    __>IMP : numbers are represented in reverse in the linked list.
    Ex:
        145 is represented as  5->4->1.
    
    resultant head is expected in the same format.
    
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
def addBoth(head_a,head_b):
    if not head_a:
        return head_b
    elif not head_b:
        return head_a
    
    carry = 0
    result = None
    tail = None

    while head_a and head_b:
        node = Node(head_a.data + head_b.data + carry)
        carry = 0
        
        if node.data > 9:
            carry = 1
            node.data -= 10
            
        if not result:
            result = node
            tail = node
        else:
            tail.next = node
            tail = node
        
        head_a = head_a.next
        head_b = head_b.next
    
    while head_a:
        node = Node(head_a.data + carry)
        carry = 0
        
        if node.data > 9:
            carry = 1
            node.data -= 10
        
        tail.next = node
        tail = node
        head_a = head_a.next
    
    while head_b:
        node = Node(head_b.data + carry)
        carry = 0
        
        if node.data > 9:
            carry = 1
            node.data -= 10
        
        tail.next = node
        tail = node
        head_b = head_b.next
    
    if carry == 1:
        node = Node(1)
        tail.next = node
        tail = node
    
    return result