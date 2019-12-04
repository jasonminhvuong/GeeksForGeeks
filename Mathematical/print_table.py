"""
    Print the table of a given number N. 

    Input:
    First line contains an integer, the number of test cases 'T'. T testcases
    follow. Each testcase cotains one line of input denoting N.

    Output:
    For each testcase, print the table of N upto 10.
"""
class Solution:
    def print_table(self, n):
        for i in range(1, 11):
            print(i*n, end=" ")
        print()

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        sol.print_table(n)

if __name__ == "__main__":
    main()