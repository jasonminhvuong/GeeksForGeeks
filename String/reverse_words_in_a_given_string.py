"""
    Given a String of length S, reverse the whole string without reversing the
    individual words in it. Words are separated by dots.

    Input:
    The first line contains T denoting the number of testcases. T testcases
    follow. Each case contains a string S containing characters.

    Output:
    For each test case, in a new line, output a single line containing the
    reversed String.
"""
class Solution:
    def reverse_words(self, s):
        words = s.split('.')
        print('.'.join(reversed(words)))

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        sol.reverse_words(s)

if __name__ == "__main__":
    main()