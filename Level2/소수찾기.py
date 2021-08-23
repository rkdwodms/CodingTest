#풀이 조건
#소수 : 1과 자기 자신으로만 나눠지는 수, 2부터 제곱근까지 나눴을 때 나눠지지 않는 수 
# numbers 분할 및 조합

from itertools import permutations

def solution(numbers):
    answer = []
    per = []
    nums = [n for n in numbers]
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums,i))
        
    new_nums = [int(("").join(p)) for p in per]
    
    for i in new_nums:
        if i < 2:
            continue
        chek = True
        
        for o in range(2, int(i**0.5)+1):
            if i % o == 0:
                chek = False
                break
        
        if chek == True:
            answer.append(i)
            
    

    return len(set(answer))
