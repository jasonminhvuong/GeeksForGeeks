"""
    Given a Binary Tree and two nodes value n1 and n2. The task is to find the
    lowest common ancestor of the given two nodes.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# If LCA exist, return reference to it. If
# If both n1 and n2 are not present, 
# rturn None. Else if left subtree contains any 
#  of them return pointer to left.
def lca(root, n1, n2):
    if not root:
        return None
    
    if root.data == n1 or root.data == n2:
        return root
    
    lr = lca(root.left, n1, n2)
    rr = lca(root.right, n1, n2)
    
    if lr and rr:
        return root
    elif lr:
        return lr
    elif rr:
        return rr
    
    return None  