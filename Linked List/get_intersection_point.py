"""
    There are two singly linked lists of size N and M in a system. But, due to
    some programming error the end node of one of the linked list got linked
    into one of the node of second list, forming a inverted Y shaped list.
    Write a program to get the point where two linked lists intersect each other.

    Your Task:
    The task is to complete the function intersetPoint() which finds the point
    of intersection of two linked list. The function should return data value
    of a node where two linked lists merge. If linked list do not merge at any
    point, then it shoudl return -1.

    Constraints:
    1 <= T <= 50
    1 <= N <= 100
    1 <= value <= 1000
"""
def intersetPoint(head_a,head_b):
    curr = head_a
    
    while curr:
        curr.data = -curr.data
        curr = curr.next
    
    curr = head_b
    
    while curr:
        if curr.data < 0:
            curr.data = -curr.data
            return curr
        
        curr = curr.next
    
    return -1