class Solution:
    def to_upper_words(self, s):
        return s.title()

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.to_upper_words(s))

if __name__ == "__main__":
    main()