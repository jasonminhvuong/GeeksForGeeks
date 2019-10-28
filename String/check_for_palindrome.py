class Solution:
    def is_palindrome(self, s, n):
        p1 = 0
        p2 = n-1
        
        while p1 <= p2:
            if s[p1] != s[p2]:
                return "No"
            p1 += 1
            p2 -= 1
        
        return "Yes"

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        s = input()
        print(sol.is_palindrome(s, n))

if __name__ == "__main__":
    main()