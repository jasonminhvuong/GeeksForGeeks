"""
    An string of words is given, the task is to reverse the string using stack.

    Input Format:
    The first line of input will contains an integer T denoting the no of test
    cases. Then T test cases follow. Each test case contains a string s of
    words without spaces.

    Output Format:
    For each test case ,print the reverse of the string in new line. 

    Your Task:
    Since this is a function problem, you don't need to take any input. Just
    complete the provided function.
"""
def reverse(s):
    stack = []
    result = ""
    
    for i in range(len(s)):
        ch = s[i]
        stack.append(ch)
    
    for i in range(len(s)):
        ch = stack.pop()
        result += ch
    
    return result