def solution(a, b):
    res = 0
    for i in range(len(a)):
        res = res + a[i] * b[i]
    
    return res
