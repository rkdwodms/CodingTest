def solution(numbers, target):
    start = [0]
    
    for i in numbers:
        result = []
        
        for j in start:
            result.append(j+i)
            result.append(j-i)
            
            start = result
            
    return start.count(target)
