# https://school.programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0
    routes.sort(key = lambda x : x[1])
    prev = -30000
    for i in routes:
        if i[0] > prev:
            answer += 1
            prev = i[1]
            
    
    return answer
