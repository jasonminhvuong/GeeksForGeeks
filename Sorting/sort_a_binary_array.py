"""
    Given a binary array A[] of size N. The task is to arrange array in
    increasing order.

    Note: The binary array contains only 0  and 1.

    Input:
    The first line of input contains an integer T, denoting the testcases.
    Every test case contains two lines, first line is N(size of array) and
    second line is space separated elements of array.

    Output:
    Space separated elements of sorted arrays. There should be a new line
    between output of every test case.
"""
class Solution:
    def sort_binary(self, n, arr):
        count = 0
        
        for i in range(n):
            if arr[i] == 0:
                print("0", end=" ")
            else:
                count +=1
        
        for _ in range(count):
            print("1", end=" ")
        
        print()
        

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        sol.sort_binary(n, arr)

if __name__ == '__main__':
    main()