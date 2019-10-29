"""
    You have been given an alphanumeric string S, extract maximum numeric value
    from that string. Alphabets will only be in lower case.

    Input:
    The first line contains a single integer T i.e. the number of test cases. T
    testcases follow. The first and only line consists of a String S.

    Output: 
    For each testcase, in a new line, print the Maximum number extracted from
    the string S.
"""
class Solution:
    def extract_max(self, s):
        num_str = ""
        curr_max = -1
        
        for ch in s:
            if ch.isnumeric():
                num_str += ch
                curr_max = max(curr_max, int(num_str))
                
            else:
                num_str = ""
                
        return curr_max

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.extract_max(s))

if __name__ == "__main__":
    main()