class Solution:
    def arr_sum(self, arr, n):
        return sum(arr)
         
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.arr_sum(arr, n))
        

if __name__ == '__main__':
    main()