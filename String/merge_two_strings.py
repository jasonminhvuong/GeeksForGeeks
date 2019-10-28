"""
    Given two strings S1 and S2 as input, the task is to merge them
    alternatively i.e. the first character of S1 then the first character
    of S2 and so on till the strings end.

    NOTE: Add the whole string if other string is empty.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. Then T test cases follow. Each test case contains two strings S1 and
    S2.

    Output:
    For each test case, in a new line, print the merged string.
"""

class Solution:
    def merge_str(self, s1, s2):
        i = 0
        result = ""
        
        while i < len(s1) and i < len(s2):
            result = result + s1[i] + s2[i]    
            i += 1
        
        result += s1[i:] + s2[i:]
        
        return result
    

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input().split()
        print(sol.merge_str(s[0], s[1]))

if __name__ == "__main__":
    main()