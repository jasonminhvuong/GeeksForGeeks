class Solution:
    def is_anagram(self, s1, s2):
        count = [0] * 256
        
        if len(s1) != len(s2):
            return "NO"
            
        for i in range(len(s1)):
            count[ord(s1[i])] += 1
            count[ord(s2[i])] -= 1
            
        for c in count:
            if c != 0:
                return "NO"
        
        return "YES"

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input().split()
        print(sol.is_anagram(s[0], s[1]))

if __name__ == "__main__":
    main()