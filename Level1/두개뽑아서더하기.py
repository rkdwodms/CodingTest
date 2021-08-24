#음수 생각하기 
# set -> 양수 정렬 후 음수 정렬
# sorted -> 음수 양수 정렬

def solution(numbers):
    
    answer = []
    for i in range(0,len(numbers)):
        for j in range(i+1, len(numbers)):
            res = numbers[i] + numbers[j]
            answer.append(res)
    
    return sorted(set(answer))
