"""
    Given a Binary Tree, your task is to print its level order traversal such
    that each level is separated by $.
"""

class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def levelOrder(root):
    '''
    :param root: root of given tree.
    :return: print the level order traversal , no need to print next line.
    '''
    if not root:
        return
    
    queue = []
    queue.append((root, 0))
    curr_height = 0
    
    while queue:
        node, h = queue.pop(0)
        
        if curr_height < h:
            print("$", end=" ")
            curr_height = h
        
        print(node.data, end=" ")
        
        if node.left:
            queue.append((node.left, h+1))
        
        if node.right:
            queue.append((node.right, h+1))
        
    print("$", end=" ")