"""
    Given an array of size N containing level order traversal of a BST. The
    task is to complete the function constructBst(), that construct the BST
    (Binary Search Tree) from its given level order traversal.

    User Task:
    Your task is to complete the function constructBst() which has two
    arguments, first as the array containing level order traversal of BST and
    next argument as the length of array.
"""
class Node:
    data=0
    left=None
    right=None

def helper(root, data):
    if not root:
        node = Node()
        node.data = data
        return node
    
    if data <= root.data:
        root.left = helper(root.left, data)
    else:
        root.right = helper(root.right, data)
    
    return root

def constructBst(arr,n):
    root = None
    
    for i in range(n):
        root = helper(root, arr[i])
    
    return root