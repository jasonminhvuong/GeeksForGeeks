"""
    Stickler the thief wants to loot money from a society having n houses in a
    single line. He is a weird person and follows a certain rule when looting
    the houses. According to the rule, he will never loot two consecutive
    houses. At the same time, he wants to maximize the amount he loots. The
    thief knows which house has what amount of money but is unable to come
    up with an optimal looting strategy. He asks for your help to find the
    maximum money he can get if he strictly follows the rule. Each house has
    a[i] amount of money present in it.

    Input:
    The first line of input contains an integer T denoting the number of
    test cases. T testcases follow. Each test case contains an integer n which
    denotes the number of houses. Next line contains space separated numbers
    denoting the amount of money in each house.

    Output:
    For each testcase, in a newline, print an integer which denotes the maximum
    amount he can take home.
"""

class Solution:
    def stickler_theif(self, arr, n):
        if not arr:
            return 0
        elif n == 1:
            return arr[0]
        elif n == 2:
            return max(arr[0], arr[1])
        
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-2]+arr[i], dp[i-1])
        
        return dp[-1]
    
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(e) for e in input().split()]
        print(sol.stickler_theif(arr, n))

if __name__ == '__main__':
    main()