#https://school.programmers.co.kr/learn/courses/30/lessons/120924

def solution(common):
    answer = 0
    if common[1] - common[0] == common[2] - common[1]:
        answer = common[-1]+(common[1]-common[0])
    elif common[1] // common[0] == common[2] //common[1]:
        answer = common[-1] * (common[1] // common[0])
    return answer
