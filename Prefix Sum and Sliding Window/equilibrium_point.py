"""
    Given an array A of N positive numbers. The task is to find the position
    where equilibrium first occurs in the array. Equilibrium position in an
    array is a position such that the sum of elements before it is equal to the
    sum of elements after it.

    Input:
    The first line of input contains an integer T, denoting the number of test
    cases. Then T test cases follow. First line of each test case contains an
    integer N denoting the size of the array. Then in the next line are N space
    separated values of the array A.

    Output:
    For each test case in a new  line print the position at which the elements
    are at equilibrium if no equilibrium point exists print -1.
"""
class Solution:
    def equilibrium_point(self, n, arr):
        total = 0
        left_sum = 0
        for i in range(n):
            total += arr[i]
            
        for i in range(n):
            total -= arr[i]
            
            if left_sum == total:
                return i+1
            
            left_sum += arr[i]
        
        return -1
    
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.equilibrium_point(n, arr))