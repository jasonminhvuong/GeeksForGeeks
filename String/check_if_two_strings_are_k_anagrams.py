"""
    Given two strings of lowercase alphabets and a value K, your task is to
    complete the given function which tells if  two strings are K-anagrams of
    each other or not.
    Two strings are called K-anagrams if both of the below conditions are true.
    1. Both have same number of characters.
    2. Two strings can become anagram by changing at most K characters in a
    string.

    Input Format:
    The first line of input contains an integer T denoting the no of test
    cases. Then T test cases follow. The first line of input contains two
    Strings Str1 and Str2. And next line contains an integer K, which denotes
    number of characters can be replaced.

    Output Format:
    For each testcase, in a new line, print the respective output.

    Your Task:
    Since this is a function problem, you don't need to take any input. Just
    complete the given function areKAnagrams that returns true if the strings
    can be turned into K-anagrams, else return false.
"""

from collections import Counter

# Your task is to complete this function
# Function should return 1/0 or True/False
def areKAnagrams(str1, str2, k):
    if len(str1) != len(str2):
        return False
    
    count = Counter()
    
    for i in range(len(str1)):
        count[str1[i]] += 1
        count[str2[i]] -= 1
    
    changes = 0
    
    for key, val in count.items():
        changes += abs(val)
    
    return k >= changes/2