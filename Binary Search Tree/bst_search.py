"""
    Given a Binary Search Tree (BST), you need to find if a particular
    node(data) is present in the BST or not. If present print 1, else print 0.
    Note: The BST does not insert duplicates

    Your Task:
    This is a function problem. you don't have to read any input. Your task is
    to complete the function search() which returns true if the node with value
    x is present in the BST else returns false.
"""

class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def search(self, node, data):
        if not node:
            return False
    
        if node.data == data:
            return True
        elif node.data > data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)