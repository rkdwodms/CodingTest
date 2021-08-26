#효율성 문제 : out of index 해결
#접근 방식 : 문자열 정렬 후 접두어 비교

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        
        # for j in range(i+1,len(phone_book)):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]:
            return False
    return True
