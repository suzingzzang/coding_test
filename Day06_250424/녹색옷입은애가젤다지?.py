# https://www.acmicpc.net/problem/4485

import sys, heapq
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dijkstra(n,cave):
    INF = int(1e9)
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] =cave[0][0]

    q = [(cave[0][0],0,0)]

    while q:
        cost,x,y = heapq.heappop(q)
        if distance[x][y] < cost:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< N and 0 <= ny < N:
                new_cost = cost + cave[nx][ny]
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] =new_cost
                    heapq.heappush(q,(new_cost,nx,ny))

    return distance[N-1][N-1]

num= 1
while True:
    N = int(input())
    if N == 0:
        break
    graph =[list(map(int,input().split())) for _ in range(N)]
    answer = dijkstra(N,graph)

    print(f"Problem {num}: {answer}")
    num+=1
