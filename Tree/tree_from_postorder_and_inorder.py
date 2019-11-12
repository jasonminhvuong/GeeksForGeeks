"""
    Given inorder and postorder traversals of a Binary Tree in the arrays in[]
    and post[] respectively. The task is to construct the binary tree from
    these traversals.
"""
def helper(In, post, inStrt, inEnd, pIndex):
    if inStrt > inEnd:
        return None
    
    node = Node(post[pIndex[0]])
    pIndex[0] -= 1
    
    # if node has no children, return node
    if inStrt == inEnd:
        return node
    
    i = 0
    for i in range(inStrt, inEnd + 1): 
        if (In[i] == node.data):  
            break
    
    node.right = helper(In, post, i+1, inEnd, pIndex)    
    node.left = helper(In, post, inStrt, i-1, pIndex)
    
    return node
    
def buildTree(In, post, n):
    '''
    :param In: given in order array
    :param post: given post order array
    :param n: number of nodes in tree
    :return: root of the created tree 
    '''
    pIndex = [n-1]
    return helper(In, post, 0, n-1, pIndex)