"""
    Given a binary tree, count leaves in it.

    Input:
    The task is to complete the method which takes one argument, root of
    Binary Tree. The struct Node has a data part which stores the data, pointer
    to left child and pointer to right child. There are multiple test cases.
    For each test case, this method will be called individually.

    Output:
    The function should return count of leaves
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# your task is to complete this function
# function should return the count of Leaf node's
# Note: You required to print a new line after every test case
def countLeaves(root):
    if not root:
        return 0
    
    if not root.left and not root.right:
        return 1
    
    return countLeaves(root.left) + countLeaves(root.right)