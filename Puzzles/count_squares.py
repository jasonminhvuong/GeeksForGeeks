"""
    Given a sample space S consisting of all perfect squares starting from 1,
    4, 9 and so on. You are given a number N, you have to print the number of
    integers less than N in the sample space S.

    Input :
    The first line contains an integer T, denoting the number of test cases.
    Then T test cases follow. The first line of each test case contains an
    integer N, denoting the number.

    Output :
    Print the answer of each test case in a new line.
"""
import math

class Solution:
    def count_squares(self, n):
        return int(math.sqrt(n-1))

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        print(sol.count_squares(n))

if __name__ == '__main__':
    main()