"""
    Given an array, write a program that prints 1 if array represents Inorder
    traversal of a BST, else prints 0. Note that all keys in BST must be
    unique.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. The first line of each test case is N, N is the size of array. The
    second line of each test case contains N input C[i].

    Output:
    Print 1 array represents BST, else 0.
"""
class Solution:
    def is_inorder_bst(self, arr, n):
        for i in range(n-1):
            if arr[i] >= arr[i+1]:
                return "0"
        
        return "1"
    
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.is_inorder_bst(arr, n))

if __name__ == "__main__":
    main()