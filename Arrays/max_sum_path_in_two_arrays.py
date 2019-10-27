"""
    Given two sorted arrays A and B. The task is to complete the function
    max_path_sum that takes 4 argument, the first two arguments represent
    the 2 arrays A[] and B[] and the last two arguments l1, l2 denote the size
    of array A and B respectively. The function returns the sum of the maximum
    sum path to reach from beginning of any array to end of any of the two
    arrays.

    Note: You can switch from one array to another array only at common
    elements.

    Input:
    The first line of input contains an integer T denoting the no of test
    cases. Then T cases follow.
    Each test case contains 3 lines. The first line contains two space
    separated integers l1 and l2 denoting the length of the two sorted array
    A and B. In the second line is the space separated values of array A and
    in the third line are space separated values of array B.

    Output:
    For each test case the output is the max sum obtained in such fashion.
"""
#Your task is to complete this function
#Function should return an integer denoting the required answer
def maxSumPath(arr1, arr2, m, n):
    sum1 = 0
    sum2 = 0
    result = 0
    i, j = 0, 0
    
    while (i < m and j < n): 
        if arr1[i] < arr2[j]: 
            sum1 += arr1[i] 
            i+=1
        elif arr1[i] > arr2[j]: 
            sum2 += arr2[j] 
            j+=1
        else:
            result += max(sum1,sum2) 
            sum1, sum2 = 0, 0

            while (i < m and j < n and arr1[i]==arr2[j]): 
                result += arr1[i] 
                i+=1
                j+=1
    
    while i < m: 
        sum1 += arr1[i] 
        i+=1

    while j < n: 
        sum2 += arr2[j] 
        j+=1

    result += max(sum1,sum2) 
      
    return result