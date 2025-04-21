# https://www.acmicpc.net/problem/2606

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    visited[start] = True
    q = deque([start])
    cnt = 0

    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append(next_node)
                visited[next_node] = True
                cnt += 1
    return cnt
print(bfs(1))

