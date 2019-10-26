from collections import Counter
class Solution:
    def majority_elem(self, arr, n):
        if not arr:
            return -1
        
        count = Counter(arr)
        most_common = count.most_common(1)[0]
        
        if most_common[1] > int(n/2):
            return most_common[0]
        else:
            return -1
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.majority_elem(arr, n))
        

if __name__ == '__main__':
    main()