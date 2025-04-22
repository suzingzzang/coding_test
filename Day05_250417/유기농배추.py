# https://www.acmicpc.net/problem/1012

k = int(input())
result = []
dy = [-1,1,0,0]
dx = [0,0,-1,1]

def dfs(y, x):
    graph[y][x] = 0  
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
            dfs(ny, nx)   
    
for _ in range(k):
    m , n , num = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    for _ in range(num):
        x , y = map(int,input().split())
        graph[y][x] =1
    cnt = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] == 1:
                dfs(y,x)
                cnt +=1
    result.append(cnt)

for _ in range(len(result)):
    print(result[_])


    
    
