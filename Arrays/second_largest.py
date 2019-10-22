class Solution:
    def second_largest(self, arr, n):
        first = max(arr)
        arr.remove(first)
        return max(arr)
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.second_largest(arr, n))
        

if __name__ == '__main__':
    main()