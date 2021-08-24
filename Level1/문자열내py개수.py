def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0
    
    s = s.upper()
    s_new = [i for i in s]
    
    for i in s_new:
        if i == 'P':
            p_cnt += 1
        if i == 'Y':
            y_cnt += 1
            
    if p_cnt == y_cnt:
        return True
    else:
        return False
