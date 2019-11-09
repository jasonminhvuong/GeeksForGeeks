"""
    Given a Binary Tree, print Left view of it. Left view of a Binary Tree is
    set of nodes visible when tree is visited from Left side. The task is to
    complete the function leftView(), which accepts root of the tree as
    argument.
"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def helper(root, level, max_level):
    if not root:
        return
    
    if max_level[0] < level:
        print(root.data, end=" ")
        max_level[0] = level
    
    helper(root.left, level+1, max_level)
    helper(root.right, level+1, max_level)

def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    helper(root, 1, [0])