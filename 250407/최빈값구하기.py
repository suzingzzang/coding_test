# https://school.programmers.co.kr/learn/courses/30/lessons/120812

def solution(array):
    answer = 0
    temp_list = []
    array_= list(set(array))
    for i in array_:
        temp_list.append(array.count(i))
    if temp_list.count(max(temp_list)) > 1:
        return -1
    else :
        answer = temp_list.index(max(temp_list))
    return array[answer]
