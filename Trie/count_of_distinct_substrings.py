"""
    Given a string of length N of lowercase alphabet characters. The task is to
    complete the function countDistinctSubstring(), which returns the count of
    total number of distinct substrings of this string.

    Input:
    The first line of input contains an integer T, denoting the number of test
    cases. Then T test cases follow. Each test case contains a string str.

    Output:
    For each test case in a new line, output will be an integer denoting count
    of total number of distinct substrings of this string.

    User Task:
    Since this is a functional problem you don't have to worry about input,
    you just have to complete the function countDistinctSubstring().

"""

class TreeNode:
    def __init__(self):
        self.is_end = False
        self.children = {}

class SuffixTree:
    def __init__(self):
        self.root = TreeNode()
        self.count = 0

    def insert(self, word):
        node = self.root

        for ch in word:
            if ch not in word.children:
                word.children[ch] = TreeNode()
                self.count += 1
            
            node = node.children[ch]
        
        node.is_end = True

class Solution:
    def count_distinct_substrs(self, s):
        t = SuffixTree()

        for i in range(len(s)):
            t.insert(s[i:])
    
        return t.count
