# https://softeer.ai/app/assessment/index.html?xid=462240&xsrfToken=K3XblYfSES506gGsk1p2ZociMxkBdYC6&testType=practice

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
zone= [[0]*N for _ in range(N)]
zone_id = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(ax,ay,zond_id):
    q = deque()
    q.append((ax,ay))
    zone[ax][ay] = zone_id
    num_list = {graph[ax][ay]}
    count = 1
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<= nx < N and 0 <= ny < N:
                if zone[nx][ny] == 0 and graph[nx][ny] not in num_list:
                    zone[nx][ny] = zone_id
                    q.append((nx,ny))
                    num_list.add(graph[nx][ny])
                    count += 1
    return count == N

for i in range(N):
    for j in range(N):
        if zone[i][j] == 0:
            if bfs(i,j,zone_id):
                zone_id +=1

for k in zone:
    print(*k)
    /////////////////////////////////////////////////////////
    import sys
input = sys.stdin.readline

n = int(input()) 
for i in range(n):
    print(' '.join([str(i+1)] * n))
