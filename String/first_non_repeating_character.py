"""
    Given a string S consisting of lowercase Latin Letters. Find the first
    non repeating character in S.

    Input:
    The first line contains T denoting the number of testcases. Then follows
    description of testcases. Each case begins with a single integer N denoting
    the length of string. The next line contains the string S.

    Output:
    For each testcase, print the first non repeating character present in
    string. Print -1 if there is no non repeating character.
"""

from collections import Counter
class Solution:
    def non_repeating_chars(self, s):
        count = Counter()
        for i in range(len(s)):
            count[s[i]] += 1
            
        for i in range(len(s)):
            if count[s[i]] == 1:
                print(s[i])
                return
        
        print("-1")

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        s = input()
        sol.non_repeating_chars(s)

if __name__ == "__main__":
    main()