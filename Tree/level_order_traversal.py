"""
    Your Task:
    You don't have to take any input. Just complete the function levelOrder()
    that takes node as parameter and prints the level order. The newline is
    automatically appended by the driver code.
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Your task is to complete this function
# Function should print the level order of the tree in required format
# only input to function is the root of the tree
def levelOrder( root ):
    if not root:
        return
    
    queue = []
    queue.append(root)
    
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        
        if node.left:
            queue.append(node.left)
        
        if node.right:
            queue.append(node.right)