"""
    You are given an array A of size N. You need to find all pairs in the array
    that sum to a number K. If no such pair exists then output will be -1. The
    elements of the array are distinct and are in sorted order.
    Note: (a,b) and (b,a) are considered same. Also, an element cannot pair
    with itself, i.e., (a,a) is invalid.

    Input:
    The first line of input is T denoting the number of testcase. T testcases
    follow. Each testcase contains three lines of input. The first line is the
    size of array N. The second line contains N elements separated by spaces.
    The third line contains the sum K.

    Output:
    For each testcase, print all the pairs such that there sum is equal to K.
"""

class Solution:
    def pairs_with_sum(self, arr, n, k):
        flag = 0
        start, end = 0, n-1
        while start < end:
            if arr[start] + arr[end] == k:
                flag = 1
                print(arr[start],arr[end],k)
                start += 1
                end -= 1
            elif arr[start] + arr[end] < k:
                start += 1
            else:
                end -= 1
        if flag == 0:
            print(-1)

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        k = int(input())
        sol.pairs_with_sum(arr, n, k)
        

if __name__ == '__main__':
    main()