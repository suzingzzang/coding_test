# https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def bfs(graph , node , visited):
    visited[node] = True
    que = deque(graph)
    while que:
        node = que.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
    return visited
        
def solution(n, wires):
    answer = -1
    # wires의 간선을 하나씩 지우면서 list 생성 그때의 순열 사이클 len return -> max값 선택
    # bfs로도 구현해보기
    len_list = []
    for i in range(len(wires)):
        len_list = wires.pop(i)
        visited = [False] * len(len_list)
        for j in range(len(len_list)):
            if not visited[j]:
                bfs(len_list ,  , visited)
            print(visited)
    return answer
