"""
    You are in a party of N people, where only one person is known to everyone.
    Such a person may be present in the party, if yes, (s)he doesn’t know
    anyone in the party. Your task is to find the stranger (celebrity) in
    party.
    You will be given a square matrix M[][] where if an element of row i and
    column j  is set to 1 it means ith person knows jth person. You need to
    complete the function getId() which finds the id of the celebrity if
    present else return -1. The function getId() takes two arguments, the
    square matrix M and its size N.

    Note: Expected time complexity is O(N) with constant extra space.

    User Task:
    The task is to complete the function getId() which returns the Id of 
    celebrity if present, else -1.    
"""
'''
Function Arguments :
		@param  :m (boolean matrix of size n*n), n(no of rows and cols)
		@return : Integer
'''
def getId(m,n):
    stack = [i for i in range(n)]
    
    while len(stack) > 1:
        i = stack.pop()
        j = stack.pop()
        
        if m[i][j] == 0 and m[j][i] == 1:
            stack.append(i)
        elif m[i][j] == 1 and m[j][i] == 0:
            stack.append(j)
    
    if len(stack) != 1:
        return -1
        
    result = stack.pop()
    
    for i in range(n):
        if i == result:
            continue
        elif m[i][result] != 1 or m[result][i] != 0:
            return -1
        
    return result