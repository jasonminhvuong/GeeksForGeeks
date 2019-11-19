"""
    Given a binary tree, return true if it is BST, else false. For example,
    the following tree is not BST, because 11 is in left subtree of 10. The
    task is to complete the function isBST() which takes one argument, root
    of Binary Tree.

    User Task:
    Since this is a functional problem you don't have to worry about input, you
    just have to complete the function isBST().
"""

import sys

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Your task is to complete this function
# Function should return an 1/0 or True/False
def helper(root, lo, hi):
    if not root:
        return True
    
    if root.data < lo or root.data > hi:
        return False
        
    left = helper(root.left, lo, root.data)
    right = helper(root.right, root.data, hi)
    
    return left and right

def isBST(root):
    return helper(root, -sys.maxsize, sys.maxsize)