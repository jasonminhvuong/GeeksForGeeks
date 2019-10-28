"""
    Given a string S containing only lower case alphabets, the task is to sort
    it in lexigraphically-descending order.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. Then T test cases follow. Each test case contains a string S.

    Output:
    For each test case, in a new line, print the sorted string.
"""
class Solution:
    def descending_order(self, s):
        chars = [c for c in s]
        chars.sort(reverse=True)
        return "".join(chars)

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.descending_order(s))

if __name__ == "__main__":
    main()