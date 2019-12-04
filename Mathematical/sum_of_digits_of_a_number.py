"""
    Write a program to check if the sum of digits of a given number N is a
    palindrome number or not.

    Input:
    The first line of the input contains T denoting the number of testcases. T
    testcases follow. Then each of the T lines contains single positive integer
    N denoting the value of number.

    Output:
    For each testcase, in a new line, output "YES" if pallindrome else "NO".
    (without the quotes)
"""
class Solution:
    def is_digit_sum_palindrome(self, n):
        total = 0
        
        for i in range(len(n)):
            total += int(n[i])
        
        total_str = str(total)
        left = 0
        right = len(total_str)-1
        
        while left < right:
            if total_str[left] != total_str[right]:
                return "NO"
            
            left += 1
            right -= 1
        
        return "YES"
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = input()
        print(sol.is_digit_sum_palindrome(n))

if __name__ == '__main__':
    main()