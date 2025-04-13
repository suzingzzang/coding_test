# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    phone_book.sort()
    for i,j in zip(phone_book,phone_book[1:]):
        if j.startswith(i):
            return False
        
    return True
