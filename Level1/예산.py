# 풀이방법 : 최대한 많은 부서에 지원하기 위해 예산에서 작은 지원금부터 빼기 + budget이 0 미만일때까지 
# from itertools import permutations

# def solution(d, budget):
#     p_max = 0
#     per = []
#     for i in range(1,len(d)+1):
#         per += list(permutations(d,i))
        
#     for i in range(len(per)):
#         if sum(per[i]) <=budget:
#             if len(per[i]) >= p_max:
#                 p_max = len(per[i])
    
#     answer = p_max
#     return answer


def solution(d, budget):
    answer = 0
    
    for i in sorted(d):
        budget = budget - i
        if budget < 0:
            break
        answer += 1
    

    return answer
