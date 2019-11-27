"""
    Given elements as nodes of the two linked lists. The task is to multiply
    these two linked lists, say L1 and L2. 
    Note: The output could be large take modulo 109+7.

    User Task:
    The task is to complete the function multiplyTwoLists() which should
    multiply the given two linked lists and return the result.
"""
MOD = 10**9+7
# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list
'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''
def multiplyTwoList(head1, head2):
    n1 = head1.data
    n2 = head2.data
    
    curr1 = head1.next
    curr2 = head2.next
    
    while curr1:
        n1 *= 10
        n1 += curr1.data
        curr1 = curr1.next
    
    while curr2:
        n2 *= 10
        n2 += curr2.data
        curr2 = curr2.next
    
    return (n1 * n2) % MOD