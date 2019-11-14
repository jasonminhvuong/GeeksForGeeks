"""
    Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place.
    The left and right pointers in nodes are to be used as previous and next
    pointers respectively in converted DLL. The order of nodes in DLL must be
    same as Inorder of the given Binary Tree. The first node of Inorder
    traversal (left most node in BT) must be head node of the DLL.

    Your Task:
    You don't have to take input. Complete the function bToDLL() that takes
    node and head as parameter. The driver code prints the DLL both ways.
"""

class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def bToDLL(root):
    head = [None]
    prev = [None]
    helper(root, prev, head)
    return head[0]

def helper(root, prev, head):
    if not root:
        return
    
    helper(root.left, prev, head)
    
    if prev[0]:
        prev[0].right = root
        root.left = prev[0]
    else:
        head[0] = root
        
    prev[0] = root
    helper(root.right, prev, head)