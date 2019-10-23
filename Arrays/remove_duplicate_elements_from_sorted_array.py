#Your function should return an integer denoting the size of the new list
def remove_duplicate(n, arr):
    if not arr:
        return 0
    elif n == 1:
        return 1
    
    j = 0
    
    for i in range(n-1):
        if arr[i] != arr[i+1]:
            arr[j] = arr[i]
            j += 1
            
    arr[j] = arr[n-1]
    j += 1
    
    return j