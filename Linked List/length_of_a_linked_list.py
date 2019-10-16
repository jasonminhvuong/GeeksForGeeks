"""
    Given a singly linked list. The task is to find the length of linked list,
    where length is defined as number of nodes in the linked list.

    Input:
    First line of input contains number of testcases T. For each testcase,
    first line of input contains number of nodes N, to be inserted into the
    linked list and next line contains data of N nodes.

    Output:
    There will be a single line of output for each testcase, which contains
    length of the linked list.
"""

'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
Your task is to return the count of elements
in the given linked list
Function Arguments: head_node (head of the linked list)
Return Type: Integer
	Contributed By: Nagendra Jha
'''
def getCount(head_node):
    if not head_node:
        return 0
        
    curr = head_node
    count = 0
    
    while curr:
        count += 1
        curr = curr.next
    
    return count