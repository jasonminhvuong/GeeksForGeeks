"""
    Given an array A of N elements. Find the majority element in the array.
    A majority element in an array A of size N is an element that appears more
    than N/2 times in the array.

    Input:  
    The first line of the input contains T denoting the number of testcases.
    The first line of the test case will be the size of array and second line
    will be the elements of the array.

    Output: 
    For each test case the output will be the majority element of the array.
    Output "-1" if no majority element is there in the array.
"""

from collections import Counter
class Solution:
    def majority_elem(self, arr, n):
        if not arr:
            return -1
        
        count = Counter(arr)
        most_common = count.most_common(1)[0]
        
        if most_common[1] > int(n/2):
            return most_common[0]
        else:
            return -1
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.majority_elem(arr, n))
        

if __name__ == '__main__':
    main()