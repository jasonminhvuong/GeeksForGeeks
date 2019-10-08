"""
    Given a string S. The task is to print all permutations of a given string.

    Input:
    The first line of input contains an integer T, denoting the number of test
    cases. Each test case contains a single string S in capital letter.

    Output:
    For each test case, print all permutations of a given string S with single
    space and all permutations should be in lexicographically increasing order.
"""

class Solution:
    def insert_between(self, l, c):
        result = []
        
        for s in l:
            for i in range(len(s)+1):
                new_s = s[:]
                
                if i == len(s):
                    new_s = new_s + c
                else:
                    new_s = new_s[:i] + c + new_s[i:]
                
                result.append(new_s)
        
        return result
    
    def permute(self, s):
        if s == "":
            return []
        elif len(s) == 1:
            return [s]
            
        c = s[-1]
        s = s[:-1]
        
        prev_perm = self.permute(s)
        return self.insert_between(prev_perm, c)
        
        
def main():
    n = int(input())
    sol = Solution()
    
    for _ in range(n):
        t = input()
        result = sol.permute(t)
        
        result.sort()
        
        for i in range(len(result)):
            s = result[i]
            if i == len(result)-1:
                print(s, end="")
            else:
                print(s, end=" ")
        print()

if __name__ == '__main__':
    main()
    