"""
    Print a sequence of numbers starting with N, without using loop,
    in which  A[i+1] = A[i] - 5,  if  A[i]>0, else A[i+1]=A[i] + 5
    repeat it until A[i]=N.

    Input:
    The first line contains an integer T, number of test cases.
    Then following T lines contains an integer N.

    Output:
    For each test case, print the pattern in newline with space separated
    integers.

    We basically first reduce 5 one by one until we reach a negative or 0.
    After we reach 0 or negative, we one by one add 5 until we reach N.
"""

class Solution:
    def print_pattern(self, x):
        print(x, end=" ")
        
        if x <= 0:
            return
        
        self.print_pattern(x-5)
        print(x, end=" ")

def main():
    n = input()
    s = Solution()
    
    for i in range(int(n)):
        x = input()
        s.print_pattern(int(x))
        print()

if __name__ == '__main__':
    main()