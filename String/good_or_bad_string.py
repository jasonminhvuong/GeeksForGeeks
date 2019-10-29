"""
    In this problem, a String S is composed of lowercase alphabets and wildcard
    characters i.e. '?'. Here, '?' can be replaced by any of the lowercase
    alphabets. Now you have to classify the given String on the basis of
    following rules:

    If there are more than 3 consonants together or more than 5 vowels together,
    the String is considered to be "BAD". A String is considered "GOOD" only
    if it is not “BAD”.

    Input:
    The first line consists of an integer T i.e number of test cases. T
    testcases follow. The first and only line of each test case consists of a
    string S. 

    Output:
    For each testcase, in a new line, print "1"  if string is GOOD, else print
    "0".
"""

class Solution:
    def is_good_str(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        v_count = 0
        c_count = 0
        
        for ch in s:
            if ch in vowels:
                v_count += 1
                c_count = 0
            elif ch == '?':
                v_count += 1
                c_count += 1
            else:
                v_count = 0
                c_count += 1
            
            if v_count > 5 or c_count > 3:
                return 0
                
        return 1

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.is_good_str(s))

if __name__ == "__main__":
    main()