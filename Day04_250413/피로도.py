# https://school.programmers.co.kr/learn/courses/30/lessons/87946#

from collections import deque
from itertools import permutations
    
def solution(k, dungeons):
    
    graph = deque(permutations(dungeons,len(dungeons)))
    max_list = []
    

    
    while graph:
        
        temp_k = k
        answer = 0
        dungeon = graph.popleft()
        
        for i in range(len(dungeon)):

            if dungeon[i][0] <= temp_k:
                temp_k -= dungeon[i][1]
                answer += 1    
                if i == len(dungeon)-1:
                    max_list.append(answer)
            else:
                
                max_list.append(answer)

    return max(max_list)
