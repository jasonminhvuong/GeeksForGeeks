"""
Given a binary tree, you need to compute the length of the diameter of the
tree. The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.
"""

# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def helper(self, root):
        if not root:
            return 0, 0
        
        ll, lm = self.helper(root.left)
        rl, rm = self.helper(root.right)
        
        return max(ll+1, rl+1), max(max(ll+rl+1, lm), rm)
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        mx = self.helper(root)[1]
        
        return mx-1 if mx > 0 else mx