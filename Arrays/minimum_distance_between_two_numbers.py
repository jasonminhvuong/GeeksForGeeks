"""
    You are given an array A, of N elements. You need to find minimum distance
    between given two integers x and y.

    Distance: The distance (index-based) between two elements of the array.

    Input Format:
    The first line of input contains an integer T, denoting the number of test
    cases. Then T test cases follow. Each test case consists of three lines.
    The first line of each test case contains an integer N denoting size array.
    Then in the next line are N space separated values of the array A. The last
    line of each test case contains two integers x and y.

    Output Format:
    For each test case, print the required answer.

    Your Task:
    Your task is to complete the function minDist which returns  an integer
    denoting the minimum distance between two integers x and y in the array.
    If no such distance is possible then return -1.
"""

import sys
# your task is to complete this function
# function should return an integer
def minDist(arr, n, x, y):
    min_dist = sys.maxsize
    prev = -1
    found_pair = False
    
    for i in range(len(arr)):
        if arr[i] == x or arr[i] == y:
            prev = i
            break
    
    if prev == -1:
        return -1
    
    for i in range(len(arr)):
        elem = arr[i]
        if elem == x or elem == y:
            if elem == arr[prev]:
                prev = i
            else:
                found_pair = True
                min_dist = min(i - prev, min_dist)
                prev = i
    
    return min_dist if found_pair else -1