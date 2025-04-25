# https://www.acmicpc.net/problem/1238

import heapq , sys
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
            new_cost = dist + cost
            if new_cost < distance[next_node]:
                distance[next_node] = new_cost
                heapq.heappush(q,(new_cost,next_node))

    return distance

N , M, X = map(int,input().split())
graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,t = map(int,input().split())
    graph[a].append((b,t))
    rev_graph[b].append((a,t))

go = dijkstra(X,graph,N)
back = dijkstra(X,rev_graph,N)

max_time = 0
for i in range(1,N+1):
    total = go[i] + back[i]
    max_time= max(max_time,total)
print(max_time)
