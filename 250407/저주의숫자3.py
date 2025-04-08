# https://school.programmers.co.kr/learn/courses/30/lessons/120871

def solution(n):
    answer = 0
    for i in range(1,n+1):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer): #if문으로 계속 돌림...
            answer += 1
    return answer
