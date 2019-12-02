"""
    Implement a Stack using two queues q1 and q2.

    Your Task:
    Since this is a function problem, you don't need to take inputs. Just
    complete the provided functions push() and pop().
"""

'''
    :param x: value to be inserted
    :return: None
    queue_1 = [] # first queue
    queue_2 = [] # second queue
    '''
def push_in_stack(x):
    
    # global declaration
    global queue_1
    global queue_2
    
    queue_1.append(x)
    
def pop_from_stack():
    '''
    :return: the value of top of stack and pop from it.
    '''
    
    # global declaration
    global queue_1
    global queue_2
    
    if not queue_1:
        return -1
    
    queue_2 = []
    
    while len(queue_1) > 1:
        item = queue_1.pop(0)
        queue_2.append(item)
        
    result = queue_1.pop(0)
    
    temp = queue_2
    queue_2 = queue_1
    queue_1 = temp
    
    return result