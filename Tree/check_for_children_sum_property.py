"""
    Given a binary tree, complete the function that returns true if the tree
    satisfies the following property: For every node, data value must be equal
    to the sum of data values in left and right children. Consider data value
    as 0 for NULL child.  Also, leaves are considered to follow the property.

    Input Format:
    The first line consists of T test cases. The first line of every test case
    consists of N, denoting the number of edges in the tree. The second and
    third line of every test case consists of N, nodes of the binary tree.

    Output Format:
    Return 1 if the given tree satisfies the given property else return 0.
"""

# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

def isSumProperty(root):
    '''
    :param root: root of the given tree.
    :return: 1 or 0 , as per the above statement
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
        return 1
        
    if not root.left and not root.right:
        return 1
        
    sum = 0
    
    if root.left:
        sum += root.left.data
    
    if root.right:
        sum += root.right.data
    
    if sum == root.data and \
        isSumProperty(root.left) and \
        isSumProperty(root.right):
            return 1
    else:
        return 0