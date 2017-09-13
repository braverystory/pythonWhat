# def prime3(n):
#     if n <= 1: return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

def prime3(n):
    if n <= 1: return False
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i += 1
    return True
