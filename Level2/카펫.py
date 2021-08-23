#풀이조건
# brown 세로는 최소 3 이상, 
# brown 가로는 total에서 세로 나누기 
# brown 가로세로에 의한 yellow의 넓이가 동일하다면 정답.

def solution(brown, yellow):
    total = brown + yellow
    for b in range(3, total+1 ):
        if total % b == 0:
            a = total//b
            if yellow == (a-2)*(b-2):
                return [a,b]
