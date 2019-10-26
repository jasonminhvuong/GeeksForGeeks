"""
    Given an array A of N integers, Your task is to complete the function
    find3Numbers which finds any 3 elements in it such that
    A[i] < A[j] < A[k] and i < j < k. You need to return them as a vector, if
    no such element is present then return the empty vector of size 0.

    Input:
    The first line of input contains an integer T denoting the no of test
    cases. Then T test cases follow. The first line of each test case contains
    an integer N denoting the size of the array A in the next line are N space
    separated values of the array A.

    Output:
    For each test case in a new line output will be 1 if the sub-sequence
    returned by the function is present in array A else 0.
"""

#Your task is to complete this function
#Your function should return a array/list containing the triplet,
#if no such triplet exist's then return empty array/list
def find3number(n, A):
    if n < 3:
        return []
    
    min_arr = []
    max_arr = []
    curr_min = A[0]
    curr_max = A[-1]
    
    for i in range(n):
        if A[i] < curr_min:
            curr_min = A[i]
            
        min_arr.append(curr_min)
        
        if A[-(i+1)] > curr_max:
            curr_max = A[-(i+1)]
        
        max_arr.insert(0, curr_max)
        
    for i in range(n):
        if A[i] > min_arr[i] and A[i] < max_arr[i]:
            return [min_arr[i], A[i], max_arr[i]]

    return []