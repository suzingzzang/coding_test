# https://www.acmicpc.net/problem/1952

import sys
input = sys.stdin.readline

M,N = map(int,input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
maps = [[0]*N for _ in range(M)]
maps[0][0] = 1
total = N*M
step = 1
x,y,tmp = 0,0,0
turn = 0
while step < total:
    nx = x+dx[tmp]
    ny = y+dy[tmp]
    if 0<= nx<M and 0<=ny<N and maps[nx][ny] == 0:
        x , y = nx, ny
        maps[x][y] =1
        step += 1
    else:
        tmp = (tmp+1)%4
        turn +=1
print(turn)
