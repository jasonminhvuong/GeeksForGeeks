"""
    Given an array A[] of N positive integers. The task is to find the maximum
    of j - i subjected to the constraint of A[i] <= A[j].

    Input:
    The first line contains an integer T, depicting total number of test cases.
    Then T test case follows. First line of each test case contains an integer
    N denoting the size of the array. Next line contains N space separated
    integeres denoting the elements of the array.

    Output:
    Print the maximum difference of the indexes i and j in a separtate line.
"""
class Solution:
    def get_max_index(self, n, arr):
        if not arr:
            return 0
        
        left_min = [0]*n
        right_max = [0]*n
        
        left_min[0] = arr[0]
        right_max[n-1] = arr[n-1]
        
        for i in range(1, n):
            left_min[i] = min(left_min[i-1], arr[i])
        
        for j in range(n-2, -1, -1):
            right_max[j] = max(right_max[j+1], arr[j])
        
        diff = -1
        i, j = 0, 0
        
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                diff = max(diff, j-i)
                j += 1
            else:
                i += 1
                
        return diff
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.get_max_index(n, arr))

if __name__ == "__main__":
    main(