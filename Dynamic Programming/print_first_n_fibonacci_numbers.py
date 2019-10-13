"""
    Given a number N, print the first N fibonacci numbers.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. Then T test cases follow. The first line of each test case contains
    the integer N.

    Output:
    Print the first n fibonacci numbers with a space between each number.
    Print the answer for each test case in a new line.
"""

class Solution:
    def fib_helper(self, n):
        if n in self.fib_cache:
            return self.fib_cache[n]
        
        val = self.fib_helper(n-2) + self.fib_helper(n-1)
        
        self.fib_cache[n] = val
        return val
        
        
    def fib(self, n):
        self.fib_cache = {1:1, 2:1}
        self.fib_helper(n)
        
        for i in range(1, n+1):
            if i == n:
                print(self.fib_cache[i])
            else:
                print(self.fib_cache[i], end=" ")
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        sol.fib(n)

if __name__ == '__main__':
    main()