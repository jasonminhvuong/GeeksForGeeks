"""
    Given an array of integers where each element represents the max number of
    steps that can be made forward from that element. The task is to find the
    minimum number of jumps to reach the end of the array (starting from the
    first element). If an element is 0, then cannot move through that element.

    Input: 
    The first line contains an integer T, depicting total number of test cases.
    Then following T lines contains a number n denoting the size of the array.
    Next line contains the sequence of integers a1, a2, ..., an.

    Output:
    For each testcase, in a new line, print the minimum number of jumps. If
    answer is not possible print "-1"(without quotes).
"""
class Solution:
    def min_jumps(self, arr, n):
        if not arr:
            return 0
        
        dp = [-1] * n
        dp[0] = 0
        
        for i in range(1, n):
            for j in range(i):
                if dp[j] != -1 and j + arr[j] >= i:
                    if dp[i] == -1:
                        dp[i] = dp[j] + 1
                    else:
                        dp[i] = min(dp[i], dp[j] + 1)
                    
                    break
                
        return dp[-1]
        
def main():
    t = int(input())
    sol = Solution()
    arr = []
    for _ in range(t):
        n = int(input())
        arr = [int(e) for e in input().split()]
        print(sol.min_jumps(arr, n))

if __name__ == '__main__':
    main()