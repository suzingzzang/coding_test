# https://www.acmicpc.net/problem/1697

from collections import deque
n , k = map(int,input().split())

def dfs(n,k):
    visited = [0]*100001
    que = deque()
    que.append(n)

    while que:
        node = que.popleft()
        if node == k :
            return visited[node]
        
        for next_node in (node+1,node-1,node*2):
            if 0<= next_node < 100001 and visited[next_node] == 0:
                visited[next_node] = visited[node] +1
                que.append(next_node)
print(dfs(n,k))
