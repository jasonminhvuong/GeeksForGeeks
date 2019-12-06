"""
    Write a program to reverse digits of a number N.

    Input:
    The first line of input contains an integer T, denoting the number of test cases. T testcases follow. Each test case contains an integer N.

    Output:
    For each test case, print the reverse digits of number N .
"""
class Solution:
    def reverse_digits(self, n):
        result = "".join(reversed(n))
        return int(result)
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = input()
        print(sol.reverse_digits(n))

if __name__ == '__main__':
    main()