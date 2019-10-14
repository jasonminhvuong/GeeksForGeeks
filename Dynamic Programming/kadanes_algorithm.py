"""
    Given an array arr of N integers. Find the contiguous sub-array with
    maximum sum.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. The description of T test cases follows. The first line of each test
    case contains a single integer N denoting the size of array. The second
    line contains N space-separated integers A1, A2, ..., AN denoting the
    elements of the array.

    Output:
    Print the maximum sum of the contiguous sub-array in a separate line for
    each test case.
"""

class Solution:
    def kadanes_algo(self, arr, n):
        if not arr:
            return 0
        
        dp = [0] * n
        dp[0] = arr[0]
        
        for i in range(1, n):
            dp[i] = max(dp[i-1]+arr[i], arr[i])
            
        return max(dp)
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(e) for e in input().split()]
        print(sol.kadanes_algo(arr, n))
    

if __name__ == '__main__':
    main()