"""
    Given an array C[], write a program that prints 1 if array is sorted in
    non-decreasing order, else prints 0.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. For each test case there will be two lines. First line contains the
    size of the array N. Second line contains N space seperated integers of the
    array C[i].

    Output:
    Print 1 if array is sorted, else print 0.
"""
class Solution:
    def is_sorted(self, n, arr):
        if n == 1:
            return 1
        
        for i in range(1, n):
            if arr[i] < arr[i-1]:
                return 0
        
        return 1

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.is_sorted(n, arr))

if __name__ == '__main__':
    main()