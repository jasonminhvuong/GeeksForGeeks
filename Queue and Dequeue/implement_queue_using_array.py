"""
    Implement a Queue using Array. Your task is only to complete the functions
    push and pop.

    Your Task :
    You are required to complete the two methods push which take one argument
    an integer 'x' to be pushed into the quee and pop which returns a integer
    poped out from othe queue.
"""
class MyQueue:
    def __init__(self):
        self.queue = []
        
    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if not self.queue:
            return -1
        
        result = self.queue.pop(0)
        return result