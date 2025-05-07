# https://www.acmicpc.net/problem/8979

import sys
input = sys.stdin.readline
N,K = map(int,input().split())
medal = [list(map(int,input().split())) for _ in range(N)]

medal.sort(key=lambda x: (-x[1],-x[2],-x[3]))


rank = 1
rank_list = {}
rank_list[medal[0][0]] = rank
prev = medal[0][1:]
for i in range(1,N):
    
    if prev == medal[i][1:]:
        rank_list[medal[i][0]] = rank
    else:
        rank = i+1
        rank_list[medal[i][0]] = rank
        prev = medal[i][1:]
        
print(rank_list[K])
