class Solution:
    def arr_reverse(self, arr, n):
        arr.reverse()
        return arr
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.arr_reverse(arr, n))
        

if __name__ == '__main__':
    main()