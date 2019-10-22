class Solution:
    def arr_rotate(self, arr, n, d):
        i = d % n
        result = arr[i:] + arr[:i]
        
        for elem in result:
            print(elem, end=" ")
        
        print()
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        params = input().split()
        n, d = int(params[0]), int(params[1])
        arr = [int(elem) for elem in input().split()]
        sol.arr_rotate(arr, n, d)
        

if __name__ == '__main__':
    main()