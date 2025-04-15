# https://school.programmers.co.kr/learn/courses/30/lessons/42839#

from itertools import permutations
def solution(numbers):
    answer = 0
    number_list = list(numbers)
    per_list = []
    for i in range(1,len(numbers)+1):
        for j in list(permutations(number_list,i)):
            if int(''.join(j)) not in per_list and int(''.join(j)) > 1:
                per_list.append(int(''.join(j)))
            
    print(per_list)
    
    for a in per_list:
        answer +=1
        for b in range(2,a):
            if a%b == 0:
                answer -= 1
                break
        
        
    return answer
