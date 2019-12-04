"""
    Given the first 2 terms A and B of an Arithmetic Series, tell the Nth term
    of the series. 

    Input:
    The first line of input contains an integer, the number of test cases T. T
    testcases follow. Each testcase in its first line should contain two
    positive integer A and B(First 2 terms of AP). In the second line of every
    testcase it contains of an integer N.

    Output:
    For each testcase, in a new line, print the Nth term of the Arithmetic
    Progression.
"""
import math
class Solution:
    def print_nth_in_gp(self, a, b, n):
        ratio = float(b)/a
        result = a
        
        for i in range(1, n):
            result *= ratio
        
        return math.floor(result)
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        a, b = list(map(int, input().strip().split()))
        n = int(input())
        print(sol.print_nth_in_gp(a, b, n))

if __name__ == '__main__':
    main()