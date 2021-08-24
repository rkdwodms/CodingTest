#a ,b의 크기에 따른 합

def solution(a, b):
    answer = 0
    if a<=b:
        for i in range(a,b+1):
            answer += i
    if a>b:
        for j in range(b, a+1):
            answer += j
        
    return answer
