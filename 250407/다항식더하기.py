# https://school.programmers.co.kr/learn/courses/30/lessons/120863#

def solution(polynomial):
    answer = ''
    temp_list = ''
    temp_list = polynomial.split(' + ')
    sum_ = 0
    sum_x = 0
    for i in range(len(temp_list)):
        if 'x' in temp_list[i]:
            if temp_list[i][:-1]:
                sum_x += int(temp_list[i][:-1])
            else:
                sum_x += 1
        else:
            sum_ += int(temp_list[i])
            print(int(temp_list[i]))
    if sum_ != 0 and sum_x != 0:
        if sum_x == 1:
            answer = 'x + ' + str(sum_)
        else:
            answer = str(sum_x) + 'x + ' + str(sum_)
    elif sum_ == 0:
        if sum_x == 1:
            answer = 'x'
        else:
            answer = str(sum_x) + 'x'
    elif sum_x == 0:
        answer = str(sum_)
        
    return answer
