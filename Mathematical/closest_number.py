"""
    Given non-zero two integers N and M. The problem is to find the number
    closest to N and divisible by M. If there are more than one such number,
    then output the one having maximum absolute value.

    Input:
    The first line consists of an integer T i.e number of test cases. T
    testcases follow.  The first and only line of each test case contains two
    space separated integers N and M.

    Output:
    For each testcase, in a new line, print the closest number to N which is
    also divisible by M.
"""
class Solution:
    def closest_num(self, n, m):
        is_negative = n < 0
        n = abs(n)
        m = abs(m)
        
        left = (n//m) * m
        right = left + m
        result = left
        
        if n == m:
            result = n
        elif n - left >= right - n:
            result = right
        
        return -result if is_negative else result
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n, m = list(map(int, input().strip().split()))
        print(sol.closest_num(n, m))

if __name__ == '__main__':
    main()