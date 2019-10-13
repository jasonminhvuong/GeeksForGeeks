"""
    There are N stairs, a person standing at the bottom wants to reach the top.
    The person can climb either 1 stair or 2 stairs at a time. Count the number
    of ways, the person can reach the top (order does matter).

    Input:
    The first line contains an integer 'T' denoting the total number of test
    cases. In each test cases, an integer N will be given.

    Output:
    For each testcase, in a new line, print number of possible ways to reach
    Nth stair. Answer your output % 10^9+7.
"""


class Solution:
    def __init__(self):
        self.dp = []
        self.dp.append(1)
        self.dp.append(2)

        for j in range(2,100001):
            self.dp.append(((self.dp[j-2])+(self.dp[j-1]))%1000000007)
        
    def climb_stairs_count(self, n):
        print(self.dp[n-1])
    
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        sol.climb_stairs_count(n)

if __name__ == '__main__':
    main()