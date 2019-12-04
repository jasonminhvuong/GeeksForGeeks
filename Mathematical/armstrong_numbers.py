"""
    For a given 3 digit number, find whether it is armstrong number or not.
    An Armstrong number of three digits is an integer such that the sum of the
    cubes of its digits is equal to the number itself. For example, 371 is an
    Armstrong number since 33 + 73 + 13 = 371

    Input:
    First line contains an integer, the number of test cases 'T'. T testcases
    follow. Each test case contains a positive integer N.

    Output:
    For each testcase, in a new line, print "Yes" if it is a armstrong number
    else print "No".
"""
class Solution:
    def is_armstrong_number(self, n):
        total = 0
        for i in range(len(n)):
            total += int(n[i])**3
        
        if total == int(n):
            return "Yes"
        else:
            return "No"
        
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = input()
        print(sol.is_armstrong_number(n))

if __name__ == '__main__':
    main()