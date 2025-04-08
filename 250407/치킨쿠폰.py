# https://school.programmers.co.kr/learn/courses/30/lessons/120884
def solution(chicken):
    answer = 0
    while True:
        service = chicken // 10
        answer += service
        chicken = chicken - (10*service) + service
        
        if chicken < 10:
            break
            
    return answer
