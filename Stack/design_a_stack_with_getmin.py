"""
    Design a data-structure SpecialStack (using the STL of stack) that supports
    all the stack operations like push(), pop(), isEmpty(), isFull() and an
    additional operation getMin() which should return minimum element from the
    SpecialStack. Your task is to complete all the functions, using stack
    data-Structure.

    Your Task:
    Since this is a function problem, you don't need to take inputs. Just
    complete the provided functions.
"""
min_stack = []

# Your task is to complete all these function's
# function should append an element on to the stack
def push(arr, ele):
    global min_stack
    
    if not arr:
        min_stack = []
    
    arr.append(ele)
    
    if not min_stack or min_stack[-1] >= ele:
        min_stack.append(ele)
    else:
        data = min_stack[-1]
        min_stack.append(data)
    
# Function should pop an element from stack
def pop(arr):
    global min_stack
    
    if not arr:
        return -1
        
    result = arr.pop()
    min_stack.pop()
    
    return result
    
# function should return 1/0 or True/False
def isFull(n, arr):
    if len(arr) == n:
        return True
    else:
        return False
    
# function should return 1/0 or True/False
def isEmpty(arr):
    return not arr
    
# function should return minimum element from the stack
def getMin(n, arr):
    global min_stack
    
    if not min_stack:
        return -1
    
    return min_stack[-1]