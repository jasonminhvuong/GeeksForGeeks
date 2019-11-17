"""
    Given a Binary Search Tree and 2 nodes value n1 and n2, your task is to
    find the lowest common ancestor(LCA) of the two nodes.
    Note: Duplicates are not inserted in the BST.

    Your Task:
    This is a function problem. You don't have to take any input. You are
    required to complete the function LCA() that takes node, n1, n2 as
    parameters and returns the node that is LCA of n1 and n2.
"""
class Node:
    def __init__(self,val):
        self.key = val
        self.left = None
        self.right = None

def helper(root, n1, n2, found, result):
    if not root:
        return False
    
    if found[0]:
        return True
    
    count = 0
    
    if root.key == n1:
        count += 1
        
    if root.key == n2:
        count += 1
    
    if helper(root.left, n1, n2, found, result):
        count += 1
    
    if helper(root.right, n1, n2, found, result):
        count += 1
    
    if not found[0] and count == 2:
        found[0] = True
        result[0] = root
    
    return count > 0

def LCA(root,n1,n2):
    '''
    :param root: given root of the bst
    :param n1: value one.
    :param n2: value two.
    :return: Lowest common Ancestor key.
    '''
    found = [False]
    result = [None]
    helper(root, n1, n2, found, result)
    
    return result[0].key