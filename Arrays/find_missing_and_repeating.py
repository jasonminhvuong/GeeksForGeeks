"""
    Given an unsorted array of size N of positive integers. One number 'A' from
    set {1, 2, …N} is missing and one number 'B' occurs twice in array.
    Find these two numbers.

    Note: If you find multiple answers then print the Smallest number found.
    Also, expected solution is O(n) time and constant extra space.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. The description of T test cases follows. The first line of each test
    case contains a single integer N denoting the size of array. The second
    line contains N space-separated integers A1, A2, ..., AN denoting the
    elements of the array.

    Output:
    Print B, the repeating number followed by A which is missing in a single
    line.
"""

class Solution:
    def find_missing_and_repeating(self, arr, n):
        for i in range(n):
            if  arr[abs(arr[i])-1] <= 0:
                print(abs(arr[i]), end=" ")
            else:
                arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
        
        for i in range(n):
            if arr[i] > 0:
                print(i+1)
            
def main():
    t = int(input())
    sol = Solution()
    inputs = []
    
    for _ in range(t):
        n = int(input())
        temp = input().split()
        for i in range(len(temp)):
            temp[i] = int(temp[i])
        
        inputs.append(temp)
    
    for arr in inputs:       
        sol.find_missing_and_repeating(arr, len(arr))
        

if __name__ == '__main__':
    main()