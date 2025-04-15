# https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product
def solution(word):
    answer = []
    for i in range(1,6):
        for j in list(product(['A','E','I','O','U'],repeat = i)):
            if j not in answer:
                answer.append(''.join(j))
    result = 0
    answer.sort()
    result = answer.index(word)+1
        
    return result
