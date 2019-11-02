"""
    Given strings s1 and s2, you need to find if s2 is a rotated version of the
    string s1. The strings are lowercase.

    Input:
    The first line of the input contains a single integer T, denoting the
    number of test cases. Then T test case follows. Each testcase contains two
    lines for s1 and s2.

    Output:
    For each testcase, in a new line, you need to print 1 if s2 is a rotated
    version of s1; else print 0.
"""
class Solution:
    def check_rotation_str(self, s1, s2):
        for i in range(len(s1)):
            s2 = s2[-1] + s2[:-1]
            
            if s1 == s2:
                return "1"
        
        return "0"

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s1 = input()
        s2 = input()
        print(sol.check_rotation_str(s1, s2))

if __name__ == "__main__":
    main()