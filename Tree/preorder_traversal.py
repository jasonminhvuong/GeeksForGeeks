"""
    User Task:
    Since this is a functional problem you don't have to worry about input,
    you just have to complete the function preorder() that prints the data in
    preorder way. The newline is automatically appended by the driver code.
"""

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def preorder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated pre order Traversal of the given tree.
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
        return
    
    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)