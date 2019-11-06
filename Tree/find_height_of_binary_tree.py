"""
    Your Task:
    You don't have to take input. Complete the function height() that takes
    node as parameter and returns the height. The printing is done by the
    driver code.
"""
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def height(root):
    '''
    :param root: root of the given tree.
    :return: Integer, height of the given binary tree
    {
        # Node Class:
        class Node:
            def __init__(self,val):
                self.data = val
                self.left = None
                self.right = None
    }
    '''
    if not root:
        return 0
        
    return max(height(root.left), height(root.right)) + 1