"""
    Find and print the uncommon characters of the two given strings S1 and S2.
    Here uncommon character means that either the character is present in one
    string or it is present in other string but not in both. The strings
    contains only lowercase characters and can contain duplicates.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. Then T test cases follow. Each test case contains two strings in two
    subsequent lines.

    Output:
    For each testcase, in a new line, print the uncommon characters of the two
    given strings in sorted order.
"""

class Solution:
    def uncommon_chars(self, s1, s2):
        set1 = set(s1)
        set2 = set(s2)
        result = set()
        
        for ch in set1:
            if ch not in set2:
                result.add(ch)
        
        for ch in set2:
            if ch not in set1:
                result.add(ch)
                
        return "".join(sorted(result))        

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s1 = input()
        s2 = input()
        print(sol.uncommon_chars(s1, s2))

if __name__ == "__main__":
    main()