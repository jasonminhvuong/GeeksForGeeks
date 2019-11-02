"""
    Given two strings A and B, find if A is a subsequence of B.

    Input:
    The first line of input contains an integer T denoting the no of test
    cases. Then T test cases follow. Each test case contains two space
    separated strings A and B.

    Output:
    For each test case, in a new line, print 1 if a is sub-sequences of b else
    print 0.
"""
class Solution:
    def check_for_subseq(self, s1, s2):
        j = 0
        for i in range(len(s2)):
            if j >= len(s1):
                break
            
            if s2[i] == s1[j]:
                j += 1
        
        if j == len(s1):
            return "1"
        else:
            return "0"
            

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input().split()
        print(sol.check_for_subseq(s[0], s[1]))

if __name__ == "__main__":
    main()