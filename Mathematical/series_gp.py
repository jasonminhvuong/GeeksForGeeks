"""
    Given the first 2 terms A and B of a Geometric Series. The task is to find
    the Nth term of the series.

    Input:
    First line contains an integer, the number of test cases 'T'. T testcases
    follow. Each test case in its first line contains two integer A and B
    (First 2 terms of GP). In the second line of every test case it contains of
    an integer N.

    Output:
    In each seperate line print the Nth term of the Geometric Progression.
    Print the floor ( floor(2.3)=2 ) of the answer. Both the terms A and B
    forms a valid GP. 
"""
class Solution:
    def print_nth_in_ap(self, a, b, n):
        diff = b-a
        result = a
        
        for i in range(1, n):
            result += diff
        
        return result
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        a, b = list(map(int, input().strip().split()))
        n = int(input())
        print(sol.print_nth_in_ap(a, b, n))

if __name__ == '__main__':
    main()