# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    sum_ = brown + yellow
    for i in range(1,sum_+1):
        if sum_ % i == 0:
            j = sum_ //i
            if (i-2)*(j-2) == yellow:
                answer = [i,j]
    return answer
