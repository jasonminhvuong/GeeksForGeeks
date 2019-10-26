"""
    Given an array of positive integers. Your task is to find the leaders in
    the array.
    Note: An element of array is leader if it is greater than or equal to all
    the elements to its right side. Also, the rightmost element is always a
    leader. 

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. The description of T test cases follows. The first line of each test
    case contains a single integer N denoting the size of array. The second
    line contains N space-separated integers A1, A2, ..., AN denoting the
    elements of the array.

    Output:
    Print all the leaders.
"""
class Solution:
    def find_leaders(self, arr, n):
        if not arr:
            return []
        elif n == 1:
            return [arr[0]]
            
        result = str(arr[-1])
        max_leader = arr[-1]
        for i in range(n-2, -1, -1):
            if arr[i] >= max_leader:
                max_leader = arr[i]
                result = str(arr[i]) + " " + result
        
        print(result)
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        sol.find_leaders(arr, n)

if __name__ == '__main__':
    main()