# https://www.acmicpc.net/problem/10282

import sys, heapq
input = sys.stdin.readline

def dijkstra(start,graph,n):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[start] = 0
    q = [(0,start)]

    while q :
        dist , now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for next_node , cost in graph[now]:
            new_cost = dist+ cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q,(new_cost,next_node))
    dist = [d for d in distance if d != INF]
    return len(dist),max(dist)

T = int(input())
for _ in range(T):
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(d):
        a,b,s = map(int,input().split())
        graph[b].append((a,s))
    count,total = dijkstra(c,graph,n)
    print(count,total)
