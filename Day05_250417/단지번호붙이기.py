# https://www.acmicpc.net/problem/2667

n = int(input())
graph = [list(map(int,input())) for _ in range(n)]

visited = [[False]*n for _ in range(n)]

def dfs(x,y):
    cnt = 1
    visited[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0<= ny< n:
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                cnt += dfs(nx,ny)
    return cnt


result = []
for row in range(n):
    for col in range(n):
        if graph[row][col] == 1 and not visited[row][col]:
            result.append(dfs(row,col))
print(len(result))
for i in range(len(result)):
    print(result[i])
