"""
    Your task is to implement  2 stacks in one array efficiently.
    
    Your Task:
    Since this is a function problem, you don't need to take any input. Just
    complete the provided functions.
"""

'''
Function Arguments :
		@param  : a (auxilary array), 
		top1 and top2 are declared as two tops of stack.
		# initialized value of  tops of the two stacks
        top1 = -1
        top2 = 101
		@return : Accordingly.
'''

def pop1(a):
    global top1
    if top1 >= 0 and top1 <= 100:
        data = a[top1]
        top1 -= 1
        return data
    
    return -1
        
def pop2(a):
    global top2
    if top2 >= 0 and top2 <= 100:
        data = a[top2]
        top2 += 1
        return data
    
    return -1
    
def push1(a,x):
    global top1
    global top2
    if top1 <= top2:
        top1 += 1
        a[top1] = x
    
def push2(a,x):
    global top1
    global top2
    if top1 <= top2:
        top2 -= 1
        a[top2] = x