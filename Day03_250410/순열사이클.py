# https://www.acmicpc.net/problem/10451
t = int(input())
def dfs(graph,node,visited):
    visited[node] = True
    for i in graph:
        if not visited[i]:
            dfs(graph , i , visited)
    return visited

for _ in range(t):
    n = int(input())
    array = [0]+list(map(int, input().split(' ')))
    visited = [False] * (n+1)
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(array,i,visited)
            cnt += 1
    print(cnt)
    
