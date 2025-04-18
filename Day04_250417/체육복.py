# https://school.programmers.co.kr/learn/courses/30/lessons/42862#

def solution(n, lost, reserve):
    answer = 0
    lost_set = sorted(set(lost) - set(reserve))
    reserve_set = sorted(set(reserve)- set(lost))
    
    for i in lost_set[:]:
        for j in reserve_set:
            if i == j +1 or i == j -1:
                answer +=1 
                reserve_set.remove(j)
                lost_set.remove(i)
                break
    
    answer = n - len(lost_set)    
    return answer
