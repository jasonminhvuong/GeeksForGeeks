class Solution:
    def count_smaller_elements(self, arr, n, x):
        count = 0
        
        for elem in arr:
            if elem <= x:
                count += 1
        
        return count
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        x = int(input())
        print(sol.count_smaller_elements(arr, n, x))
        
if __name__ == '__main__':
    main()