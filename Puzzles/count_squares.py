import math

class Solution:
    def count_squares(self, n):
        return int(math.sqrt(n-1))

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        print(sol.count_squares(n))

if __name__ == '__main__':
    main()