"""
    Given a sorted array arr[] of non-repeating integers without duplicates.
    Sort the array into a wave-like array and return it. In other words,
    arrange the elements into a sequence such that
    a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical
    order).

    Input:
    The first line contains an integer T, depicting total number of test cases.
    T testcases follow. The first line of each testcase contains an integer N
    depicting the size of the array. The second line contains N space separated
    elements of the array.

    Output:
    For each testcase, in a new line, print the array into wave-like array.
"""
class Solution:
    def wave_arr(self, arr, n):
        if n < 2:
            return " ".join(arr)
        
        for i in range(n-1):
            if i % 2 == 0:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp
            
        return " ".join(arr)
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = input().split()
        print(sol.wave_arr(arr, n))
        

if __name__ == '__main__':
    main()