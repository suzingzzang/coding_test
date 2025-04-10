# https://school.programmers.co.kr/learn/courses/30/lessons/12909


def solution(s):
    answer = True
    check_list = []
    for i in s:
        if i == "(":
            check_list.append("(")
        else:
            if not check_list:
                answer = False
                break
            if check_list.pop() == ")":
                answer = False
                break
    if check_list:
        answer = False
    return answer
