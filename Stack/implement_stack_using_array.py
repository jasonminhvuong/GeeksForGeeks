"""
    Implement a Stack using Array. Your task is to complete the functions below.

    Your Task:
    You are required to complete two methods push which take one argument an
    integer 'x' to be pushed into the stack  and pop which returns a integer
    poped out from the stack.
"""

class MyStack:
    
    def __init__(self):
        self.arr=[]
    
    #Adds element to the Stack
    def push(self,data):
        self.arr.append(data)
    
    #Removes element from the stack
    def pop(self):
        if self.arr:
            data = self.arr.pop()
            return data
        
        return -1