"""
    Given a BST and some keys, you need to insert the keys in the given BST.
    Duplicates are not inserted.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

def insertinBST(root, node):
    if not root:
        return node
    
    if node.data < root.data:
        child = insertinBST(root.left, node)
        if child == node:
            root.left = node
    elif node.data > root.data:
        child = insertinBST(root.right, node)
        if child == node:
            root.right = node
        
    return root