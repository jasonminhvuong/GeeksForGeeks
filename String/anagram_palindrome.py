"""
    Given a string S, Check if characters of the given string can be rearranged
    to form a palindrome. For example characters of “geeksogeeks” can be
    rearranged to form a palindrome “geeksoskeeg”, but characters of 
    “geeksforgeeks” cannot be rearranged to form a palindrome.

    Input:
    First line consists of integer T  denoting the number of test cases. T
    testcases follow. For each testcase there are one line of input containing
    string S.

    Output:
    For each testcase, in a new line, print "Yes" if is possible to make it
    a palindrome, else "No".
"""

class Solution:
    def is_anagram_palindrome(self, s):
        count = {}
        odd_found = len(s) % 2 == 0
        
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1
        
        for k, v in count.items():
            if v % 2 == 1 and not odd_found:
                odd_found = True
            elif v % 2 == 1:
                return "No"
        
        return "Yes"

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.is_anagram_palindrome(s))

if __name__ == "__main__":
    main()