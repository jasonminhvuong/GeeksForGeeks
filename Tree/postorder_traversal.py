"""
    Your Task:
    You don't need to take input. Just complete the function postorder() that
    takes node as parameter. The newline is automatically appended by the
    driver code.
"""
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def postOrder(root):
    '''
    :param root: root of the given tree.
    :return: None, print the space separated post order Traversal of the given tree.
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
    
        postOrder(root.left)
        postOrder(root.right)
        print(root.data, end=" ")