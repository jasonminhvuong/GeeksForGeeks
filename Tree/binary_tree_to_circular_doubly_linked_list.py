"""
    Given a Binary Tree of N edges. The task is to convert this to a Circular
    Doubly Linked List(CDLL) in-place. The left and right pointers in nodes
    are to be used as previous and next pointers respectively in converted
    CDLL. The order of nodes in CDLL must be same as Inorder of the given
    Binary Tree. The first node of Inorder traversal (left most node in BT)
    must be head node of the CDLL.
    
    Your Task:
    You don't have to take input. Complete the function bTreeToCList() that
    takes root as parameter and returns the head of the list. The printing is
    done by the driver code.
"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def bTreeToClist(root):
    prev = [None]
    head = [None]
    helper(root, prev, head)
    
    if prev[0] and head[0]:
        prev[0].right = head[0]
        head[0].left = prev[0]
    
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