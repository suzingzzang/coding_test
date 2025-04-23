# https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque
def bfs(maps,n,m):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    que = deque()
    que.append((0,0))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0<= ny <m :
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] +1
                    que.append((nx,ny))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1
    
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    answer = bfs(maps,n,m)
    
    return answer
