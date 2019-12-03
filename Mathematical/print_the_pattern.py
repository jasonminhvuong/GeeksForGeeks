"""
    You a given a number N. You need to print the pattern for the given value
    of N.
    for N=2 the pattern will be 
    2 2 1 1
    2 1
    for N=3 the pattern will be 
    3 3 3 2 2 2 1 1 1
    3 3 2 2 1 1
    3 2 1

    Your Task:
    Since this is a function problem, you don't need to worry about the
    testcases. Your task is to complete the function printPat which takes one
    argument 'N' denoting the length of the pattern.
"""
def printPat(n):
    result = ""
    for i in range(n, 0, -1):
        for j in range(n, 0, -1):
            for _ in range(i):
                result += str(j) + " "
            
        result += "$"
    
    return result