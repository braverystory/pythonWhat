
def prime1(int n):
    if n <= 1: return False
    cdef int i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
    
def prime2(n):
    if n <= 1: return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
