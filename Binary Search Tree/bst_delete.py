"""
    Given a Binary Search Tree (BST) and a node no 'x', your task is to delete
    the node 'x' from the BST.
    Note: The duplicates are not inserted in the BST.

    Your Task:
    You are required to complete the function deleteNode() which takes two
    arguments. The first being the root of the tree, and an integer 'x'
    denoting the node to be deleted from the BST. The function returns a
    pointer to the root of the modified BST.
"""

class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

def find_successor(node):
    curr = node
    
    while curr.left:
        curr = curr.left
    
    return curr

def deleteNode(root,key):
    '''
    :param root: root of the given tree
    :param x: value to be deleted
    :return: None.
    '''
    if not root:
        return root
        
    if key < root.key:
        root.left =  deleteNode(root.left, key)
    elif key > root.key:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        else:
            successor = find_successor(root.right)
            root.key = successor.key
            root.right = deleteNode(root.right, successor.key)
            
    return root