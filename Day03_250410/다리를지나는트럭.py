
#https://school.programmers.co.kr/learn/courses/30/lessons/42583?language=python3

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = [0]*bridge_length
    
    while q:
        answer+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]>weight:
                q.append(0)
            else:
                q.append(truck_weights.pop(0))
                
    return answer
