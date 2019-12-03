"""
    Given an integer K and a queue of integers, we need to reverse the order of
    the first K elements of the queue, leaving the other elements in the same
    relative order.

    Only following standard operations are allowed on queue.

    enqueue(x) : Add an item x to rear of queue
    dequeue() : Remove an item from front of queue
    size() : Returns number of elements in queue.
    front() : Finds front item.

    Your Task:
    Since this is a function problem, you don't need to take inputs. Just
    complete the provided function modifyQueue that takes queue and k as
    parameters and returns a modified queue. The printing is done automatically
    by the driver code.
"""
'''
Function Arguments :
		@param  : queue ( given queue to be used), k(Integer ),n(size of queue)
		@return : lsit, just reverse the first k elements of queue and return new queue
'''
def reverseK(queue,k,n):
    stack = []
    
    for _ in range(k):
        item = queue.pop(0)
        stack.append(item)
    
    for _ in range(k):
        item = stack.pop()
        queue.append(item)
    
    for _ in range(n-k):
        item = queue.pop(0)
        queue.append(item)
        
    return queue