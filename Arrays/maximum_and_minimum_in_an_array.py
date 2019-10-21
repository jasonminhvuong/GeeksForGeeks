class Solution:
    def find_max_and_min(self, arr, n):
        print(min(arr), max(arr))
    
def main():
    t = int(input())
    sol = Solution()
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        sol.find_max_and_min(arr, n)

if __name__ == '__main__':
    main()