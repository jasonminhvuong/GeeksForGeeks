"""
    Jarvis is weak in computing palindromes for Alphanumeric characters.
    While Ironman is busy fighting Thanos, he needs to activate sonic punch but
    Jarvis is stuck in computing palindromes.
    You are given a string S containing alphanumeric characters. Find out
    whether the string is a palindrome or not.
    If you are unable to solve it then it may result in the death of Iron Man.

    Input:
    The first line of the input contains T, the number of test cases. T
    testcases follow.  Each line of the test case contains string 'S'.

    Output:
    Each new line of the output contains "YES" if the string is palindrome and
    "NO" if the string is not a palindrome.
"""
class Solution:
    def save_ironman(self, s):
        p1 = 0
        p2 = len(s)-1
        s = s.lower()
        
        while p1 < p2:
            while p1 < p2 and not s[p1].isalnum():
                p1 += 1
                
            while p1 < p2 and not s[p2].isalnum():
                p2 -= 1
            
            if p1 >= p2:
                break
            
            if s[p1] != s[p2]:
                return "NO"
                
            p1 += 1
            p2 -= 1
        
        return "YES"

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.save_ironman(s))

if __name__ == "__main__":
    main()