# https://softeer.ai/app/assessment/index.html?xid=462549&xsrfToken=kHraLAPzmSYtvJ2IMQIzO9gfSgiTb3oZ&testType=practice

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = [list(map(int,input().strip())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    count = 1
    while q:
        ax,ay = q.popleft()
        for i in range(4):
            nx = ax + dx[i]
            ny = ay + dy[i]
            if 0<= nx < N and 0<= ny < N:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                    count += 1
    return count
result = []
for row in range(N):
    for col in range(N):
        if graph[row][col] == 1 and not visited[row][col] :
            result.append(bfs(row,col))
result.sort()
print(len(result))
for num in result:
    print(num)
