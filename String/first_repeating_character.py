"""
    Given a string S. The task is to find the first repeated character in it.
    We need to find the character that occurs more than once and whose index of
    first occurrence is smallest. S contains only lowercase letters.
    Input:
    The first line of input contains an integer T denoting the no of test
    cases. Then T test cases follow. Each test case contains a string S.

    Output:
    For each test case in a new line print the first repeating character in the
    string. If no such character exist print -1.
"""
class Solution:
    def first_repeated(self, s):
        seen = set()
        
        for i in range(len(s)):
            if s[i] in seen:
                return s[i]
            else:
                seen.add(s[i])
        
        return "-1"

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.first_repeated(s))

if __name__ == "__main__":
    main()