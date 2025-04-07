# https://school.programmers.co.kr/learn/courses/30/lessons/120923

def solution(num, total):
    answer = []
    sets = set()
    for i in range(num):
        sets_i = set()
        print(set_i)
    return answer


##################################
# 8~11라인 이해안됨
def solution(num, total):
    
    answer = []
    d = 0
    
    for i in range(1, num):
        d += i
        
    a1 = (total - d) // num
    
    for i in range(a1, a1 + num):
        answer.append(i)
    
    return answer
