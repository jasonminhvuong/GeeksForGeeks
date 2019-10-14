"""
    Given an integer N denoting the Length of a line segment. you need to cut
    the line segment in such a way that the cut length of a line segment each
    time is integer either x , y or z. and after performing all cutting
    operation the total number of cutted segments must be maximum. 

    Input
    First line of input contains of an integer 'T' denoting number of test
    cases. First line of each testcase contains N . Second line of each
    testcase contains 3 space separated integers x , y and z.

    Output
    For each test case print in a new line an integer corresponding to the
    answer.
"""

class Solution:
    def max_segments(self, n, x, y, z):
        self.dp = [-1] * (n+10)
        self.dp[0] = 0
        
        for i in range(0, n):
            if self.dp[i] != -1:
                if i+x <= n:
                    self.dp[i+x] = max(self.dp[i]+1, self.dp[i+x])
                if i+y <= n:
                    self.dp[i+y] = max(self.dp[i]+1, self.dp[i+y])
                if i+z <= n:
                    self.dp[i+z] = max(self.dp[i]+1, self.dp[i+z])
        
        return self.dp[n]
        
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        s = input().split()
        x, y, z = int(s[0]), int(s[1]), int(s[2])
        print(sol.max_segments(n, x, y, z))

if __name__ == '__main__':
    main()
