"""
    Given a Binary Tree, convert it into its mirror.
"""
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def mirror(root):
    if not root:
        return
    
    mirror(root.left)
    mirror(root.right)
    
    temp = root.left
    root.left = root.right
    root.right = temp