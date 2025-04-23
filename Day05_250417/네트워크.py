# https://school.programmers.co.kr/learn/courses/30/lessons/43162

def dfs(computers,node,visited):
    visited[node] = True
    for next_node in range(len(computers)):
        if computers[node][next_node] == 1 and not visited[next_node]:
            dfs(computers, next_node, visited)
            
def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers,i,visited)
            answer += 1
    return answer
