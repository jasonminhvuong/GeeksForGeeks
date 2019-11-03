"""
    Given two strings S1 and S2 in lowercase, the task is to make them anagram.
    The only allowed operation is to remove a character from any string.
    Find minimum number of characters to be deleted to make both the strings
    anagram. If two strings contains same data set in any order then strings
    are called Anagrams.

    Input Format:
    The first line of input contains an integer T denoting the number of test
    cases. Then T test cases follow. Each test case consists of 2 strings to
    make the anagrams.

    Output Format:
    For each testcase, in a new line, output the minimum number of characters
    to be deleted to make both the strings anagram.

    Your Task:
    Since this is a function problem, you don't need to take any input. Just
    complete the provided function.
"""

from collections import Counter
# function to calculate minimum numbers of characters
# to be removed to make two strings anagram
def remAnagram(str1, str2):
    count1 = Counter()
    count2 = Counter()
    diff = 0
    
    for i in range(len(str1)):
        count1[str1[i]] += 1
        
    for i in range(len(str2)):
        count2[str2[i]] += 1
    
    for k, v in count1.items():
        if k not in count2:
            diff += v
        elif v - count2[k] > 0:
            diff += v - count2[k]
            
    for k, v in count2.items():
        if k not in count1:
            diff += v
        elif v - count1[k] > 0:
            diff += v - count1[k]
    
    return diff