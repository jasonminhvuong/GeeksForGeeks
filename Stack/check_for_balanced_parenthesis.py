"""
    Given an expression string exp. Examine whether the pairs and the orders
    of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
    For example, the program should print 'balanced' for 
    exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”

    Input:
    The first line of input contains an integer T denoting the number of test
    cases.  Each test case consists of a string of expression, in a separate
    line.

    Output:
    Print 'balanced' without quotes if the pair of parenthesis is balanced else
    print 'not balanced' in a separate line.
"""
class Solution:
    def check_balanced(self, exp):
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}
        
        for i in range(len(exp)):
            ch = exp[i]
            
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            elif len(stack) != 0 and ch in pairs:
                top = stack.pop()
                
                if top != pairs[ch]:
                    return "not balanced"
            else:
                return "not balanced"
                
        if len(stack) != 0:
            return "not balanced"
        else:
            return "balanced"
    
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        exp = input()
        print(sol.check_balanced(exp))

if __name__ == "__main__":
    main()