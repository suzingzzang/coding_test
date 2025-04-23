# https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque
def bfs(begin,target,words,visited):
    que = deque()
    que.append((begin,0))
    while que:
        node,cnt = que.popleft()
        if node == target:
            return cnt
        for i in range(len(words)):
            if not visited[i]:
                tmp_cnt = 0
                for j in range(len(words[i])):
                    if node[j] != words[i][j]:
                        tmp_cnt +=1
                if tmp_cnt == 1:
                    visited[i] = True
                    que.append((words[i],cnt +1))                    
    return 0
                

def solution(begin, target, words):
    answer = 0
    visited = [False]* len(words)
    answer = bfs(begin,target,words,visited)
    if target not in words:
        return 0
    return answer
