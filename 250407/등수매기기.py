# https://school.programmers.co.kr/learn/courses/30/lessons/120882

def solution(score):
    answer = []
    temp_list = []
    temp=[]
    for i in score:
        temp_list.append((i[0] + i[1])/2)
        temp.append((i[0] + i[1])/2)
    temp_list.sort(reverse=True)

    for j in temp:
        answer.append(temp_list.index(j)+1)            

    return answer
