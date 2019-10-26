"""
    Find out the maximum sub-array of non negative numbers from an array.
    The sub-array should be continuous. That is, a sub-array created by
    choosing the second and fourth element and skipping the third element is
    invalid.

    Maximum sub-array is defined in terms of the sum of the elements in the
    sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).

    Example:
    A : [1, 2, 5, -7, 2, 3]
    The two sub-arrays are [1, 2, 5] [2, 3].
    The answer is [1, 2, 5] as its sum is larger than [2, 3]

    NOTE 1: If there is a tie, then compare with segment's length and return
    segment which has maximum length
    NOTE 2: If there is still a tie, then return the segment with minimum
    starting index

    Input:
    The first line contains an integer T, depicting total number of test cases. 
    Then following T lines contains an integer N depicting the size of array
    and next line followed by the value of array.

    Output:
    Print the Sub-array with maximum sum.
"""

class Solution:
    def max_sub_array(self, arr, n):
        sub_arr = []
        result = []
        sub_amount = 0
        max_seq = 0
       
        for i in range(n):
            if arr[i] < 0:
                sub_arr = []
                sub_amount = 0
            else:
                sub_arr.append(arr[i])
                sub_amount += arr[i]
                
                if max_seq < sub_amount:
                    max_seq = sub_amount
                    result = sub_arr
                elif max_seq == sub_amount:
                    if len(result) == len(sub_arr):
                        if sub_arr[0] > result[0]:
                            result = sub_arr
                    elif len(sub_arr) > len(result):
                            result = sub_arr
        
        return " ".join(map(str, result))
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.max_sub_array(arr, n))

if __name__ == '__main__':
    main()