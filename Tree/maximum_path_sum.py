"""
    Given a binary tree in which each node element contains a number. Find the
    maximum possible sum from one leaf node to another.
"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def helper(root, max_sum):
    if not root:
       return 0
    
    l_sum = helper(root.left, max_sum)
    r_sum = helper(root.right, max_sum)

    max_sum[0] = max(max_sum[0], l_sum + r_sum + root.data)
    
    return max(l_sum, r_sum) + root.data

def maxPathSum(root):
    result = [0]
    helper(root, result)
    return result[0]