"""
    Given a binary tree, connect the nodes that are at same level.

    Your Task:
    You don't have to take input. Complete the function connect() that takes
    node as parameter and connects the nodes at same level. The printing is
    done by the driver code.
"""
def connect(root):
    '''
    :param root: root of the given tree
    :return: none, just connect accordingly.
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
                self.nextRight = None
    }
    '''
    
    if not root:
        return
    
    queue = []
    queue.append((root, 0))
    curr_h = -1
    prev = None
    
    while queue:
        node, h = queue.pop(0)
        
        if h > curr_h:
            curr_h = h
        else:
            prev.nextRight = node
        
        prev = node
        
        if node.left:
            queue.append((node.left, h+1))
        
        if node.right:
            queue.append((node.right, h+1))