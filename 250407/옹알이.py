# https://school.programmers.co.kr/learn/courses/30/lessons/120956

def solution(babbling):
    answer =0
    yes = ["aya","ye","woo","ma"]
    for i in babbling:
        for j in yes:
            if j in i :
                i = i.replace(j,'-')

        i = i.replace('-','')
        if len(i) == 0:
            answer += 1
    return answer
