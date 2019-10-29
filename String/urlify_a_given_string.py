"""
    Write a method to replace all the spaces in a string S with ‘%20’. You may
    assume that the string has sufficient space (or allocated memory) at the
    end to hold the additional characters,

    Note: The leading and trailing spaces should be trimmed off and not
    replaced by %20.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. The T test cases follow. Each test case contains two lines of input.
    The first line contains a string S. The next line contains an integer K
    that denotes the length of the S with whitespace included.

    Output:
    For each testcase, in a new line, print the string with spaces replaced by
    "%20"
"""

class Solution:
    def URLify(self, s, n):
        result = ""
        s = s.strip()
        
        for ch in s:
            if ch == " ":
                result = result + "%20"
            else:
                result = result + ch
        
        return result

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        n = int(input())
        print(sol.URLify(s, n))

if __name__ == "__main__":
    main()