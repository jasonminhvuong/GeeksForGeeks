"""
    Given an array arr[] of N non-negative integers representing height of
    blocks at index i as Ai where the width of each block is 1. Compute how
    much water can be trapped in between blocks after raining.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. The description of T test cases follows. Each test case contains an
    integer N denoting the size of the array, followed by N space separated
    numbers to be stored in array.

    Output:
    Output the total unit of water trapped in between the blocks.
"""
class Solution:
    def trapping_rain(self, arr, n):
        left = [0] * n
        right = [0] * n
        result = 0
        
        left[0] = arr[0]
        for i in range(1, n):
            left[i] = max(left[i-1], arr[i])
        
        right[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], arr[i])
        
        for i in range(n):
            result += min(left[i], right[i]) - arr[i]
        
        return result
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.trapping_rain(arr, n))
        
if __name__ == '__main__':
    main()