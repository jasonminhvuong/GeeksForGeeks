"""
    Given a string S, find length of the longest substring with all distinct
    characters. For example, for input "abca", the output is 3 as "abc" is the
    longest substring with all distinct characters.

    Input:
    The first line of input contains an integer T denoting the number of test
    cases. The first line of each test case is String str.

    Output:
    Print length of smallest substring with maximum number of distinct
    characters. Note: The output substring should have all distinct characters.
"""

from collections import Counter
class Solution:
    def longest_distinct_chars(self, s):
        counter = Counter()
        count = 0
        longest = 0
        i, j = 0, 0
        
        while i < len(s):
            counter[s[i]] += 1
            count += 1
            
            while counter[s[i]] != 1 and j < i:
                counter[s[j]] -= 1
                j += 1
                count -= 1
            
            longest = max(count, longest)
            i += 1
        
        return longest

def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        s = input()
        print(sol.longest_distinct_chars(s))

if __name__ == "__main__":
    main()