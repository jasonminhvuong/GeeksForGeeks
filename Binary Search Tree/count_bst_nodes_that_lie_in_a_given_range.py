"""
    Given a Binary Search Tree (BST) and a range l-h(inclusive), count the
    number of nodes in the BST that lie in the given range.

    The values smaller than root go to the left side
    The values greater and equal to the root go to the right side

    Your Task:
    This is a function problem. You don't have to take input. You are required
    to complete the function getCountOfNode() that takes root, l ,h as
    parameters and returns the count.
"""
class Node:
    def __init__(self):
        self.data = 0
        self.left = None
        self.right = None

def getCountOfNode(root,l,h):
    if not root:
        return 0
    
    count = 0
    
    if root.data > l:
        count += getCountOfNode(root.left, l, h)
    
    if root.data < h:
        count += getCountOfNode(root.right, l, h)
        
    if root.data >= l and root.data <= h:
        count += 1
        
    return count