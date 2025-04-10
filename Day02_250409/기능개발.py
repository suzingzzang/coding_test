# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
def solution(progresses, speeds):
    answer = []
    left_day = deque()
    cnt = 1
    for i in range(len(speeds)):
        if (100-progresses[i])%speeds[i] == 0 :
            left_day.append((100-progresses[i])//speeds[i])
        else :
            left_day.append((100-progresses[i])//speeds[i]+1)
    x1 = left_day.popleft()      # 왜 while문 밖에서 꺼내야하는지...?
    while left_day:        
        x2 = left_day.popleft()
        if  x1 >= x2:
            cnt +=1
        else:
            answer.append(cnt)
            x1 = x2
            cnt = 1 
        if not left_day:
            answer.append(cnt)
    return answer
