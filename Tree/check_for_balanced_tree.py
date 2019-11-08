"""
    Given a binary tree, find if it is height balanced or not. 
    A tree is height balanced if difference between heights of left and right
    subtrees is not more than one for all nodes of tree. 
"""
class Node: 
    # Constructor to create a new Node 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None
 # This function should return tree if passed  tree 
 # is balanced, else false.  Time complexity should
 # be O(n) where n is number of nodes in tree */
def helper(root):
    if not root:
        return True, 0
    
    lt, lh = helper(root.left)
    rt, rh = helper(root.right)
    
    return lt and rt and abs(lh - rh) < 2, max(lh, rh) + 1
    
def isBalanced(root):
    result = helper(root)
    return result[0]