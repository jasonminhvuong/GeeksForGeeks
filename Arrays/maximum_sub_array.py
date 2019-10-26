class Solution:
    def max_sub_array(self, arr, n):
        sub_arr = []
        result = []
        sub_amount = 0
        max_seq = 0
       
        for i in range(n):
            if arr[i] < 0:
                sub_arr = []
                sub_amount = 0
            else:
                sub_arr.append(arr[i])
                sub_amount += arr[i]
                
                if max_seq < sub_amount:
                    max_seq = sub_amount
                    result = sub_arr
                elif max_seq == sub_amount:
                    if len(result) == len(sub_arr):
                        if sub_arr[0] > result[0]:
                            result = sub_arr
                    elif len(sub_arr) > len(result):
                            result = sub_arr
        
        return " ".join(map(str, result))
            
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        arr = [int(elem) for elem in input().split()]
        print(sol.max_sub_array(arr, n))

if __name__ == '__main__':
    main()