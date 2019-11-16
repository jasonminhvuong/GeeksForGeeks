"""
    Given an array of size N which represents the elements to be inserted into
    BST (considering first element as root). The task is to find the minimum
    element in this given BST. If the tree is empty, there is no minimum
    element, so print -1 in that case.

    User Task:
    The task is to complete the function minValue() which takes root as the
    argument and returns the minimum element of BST.
"""

def minValue(root):
    if not root:
        return -1
    
    min_val = root.data    
    
    if root.left:
        min_val = min(min_val, minValue(root.left))
    elif root.right:
        min_val = min(min_val, minValue(root.right))
    
    return min_val