# https://school.programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    temp_list = []
    for i in commands:
        temp_list=array[i[0]-1:i[1]]
        temp_list.sort()
        answer.append(temp_list[i[2]-1])
    return answer
