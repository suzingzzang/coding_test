# https://school.programmers.co.kr/learn/courses/30/lessons/120907

def solution(quiz):
    answer = []
    for i in quiz:
        le , ri = i.split(' = ')
        a, cal , b = le.split()
        if cal == '+':
            if int(a) + int(b) == int(ri):
                answer.append('O')
            else:
                answer.append('X')
        elif cal == '-':
            if int(a) - int(b) == int(ri):
                answer.append('O')
            else:
                answer.append('X')
    return answer
