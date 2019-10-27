"""
    Given an array A of size N, construct a Product Array P (of same size) such
    that P is equal to the product of all the elements of A except A[i].

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. T testcases follow. Each testcase contains two lines of input. The
    first line is N. The second line contains N elements separated by spaces.

    Output:
    For each testcase, print the Product array P.
"""
class Solution:
    def product_arr(self, arr, n):
        if n < 2:
            return " ".join(map(str, arr))
        
        left_arr = [arr[0]]
        right_arr = [arr[-1]]
        result = []
        
        for i in range(1, n):
            left_arr.append(left_arr[i-1] * arr[i])
            right_arr.insert(0, right_arr[0] * arr[-(i+1)])
        
        for i in range(n):
            if i == 0:
                result.append(right_arr[i+1])
            elif i == n-1:
                result.append(left_arr[i-1])
            else:
                result.append(left_arr[i-1] * right_arr[i+1])
        
        return " ".join(map(str, result))
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.product_arr(arr, n))
        

if __name__ == '__main__':
    main()