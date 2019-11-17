"""
    Given a Binary Search Tree (BST), modify it so that all greater values in
    the given BST are added to every node.
    In this function problem, the task is to complete the function modify which
    takes one argument: Address of the root of the BST. The function should
    contain the logic to modify the BST so that in the modified BST, every node
    has a value equal to the sum of its value in the original BST and  values
    of all the elements larger than it in the original BST.

    The BST node structure has 3 fields, a data part which stores the data, a
    left pointer which points to the left element of the BST and a right
    pointer which points to the right node of the BST. 

    There are multiple test cases. For each test case, this function will be
    called individually.
"""

def helper(root, prev_sum):
    if not root:
        return 0
    
    helper(root.right, prev_sum)
    prev_sum[0] += root.data
    root.data = prev_sum[0]
    helper(root.left, prev_sum)
    
def modifyBST(root):
    prev_sum = [0]
    helper(root, prev_sum)