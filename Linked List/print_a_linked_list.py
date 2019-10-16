"""
    You are given the pointer to the head node of a linked list. You have to
    print all of its elements in order in a single line.

    Input:
    You have to complete a method which takes one argument: the head of the
    linked list. You should not read any input from stdin/console. The struct
    Node has a data part which stores the data and a next pointer which points
    to the next element of the linked list. There are multiple test cases. For
    each test case, this method will be called individually.

    Output:
    Print the elements of the linked list in a single line separated by a
    single space.

    User Task:
    The task is to complete the function display() which prints the elements
    of the linked list.
"""

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
def printlist(node):
    if not node:
        return
    
    curr = node
    while curr.next:
        print(curr.data, end=" ")
        curr = curr.next

    print(curr.data, end="")