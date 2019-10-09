def josephus(n,k):
    if n == 1:
        return 1
    
    # +1 at the end because not 0 based
    # k-1 becuase the skipping (k) is inclusive
    return ((josephus(n-1, k) + k-1) % n) + 1