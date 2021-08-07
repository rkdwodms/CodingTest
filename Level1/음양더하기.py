def solution(absolutes, signs):
    res = 0

    for i in range(len(absolutes)):
        if signs[i] is False:
            absolutes[i] = absolutes[i] * (-1)
            res = res + absolutes[i]
        else:
            res = res + absolutes[i]
            
            
    answer = sum(absolutes)
    return answer
