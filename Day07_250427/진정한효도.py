# https://softeer.ai/app/assessment/index.html?xid=462515&xsrfToken=A3nu5ZdFa2TAC4JfCDSI4nxGydf0qO47&testType=practice

import sys
input = sys.stdin.readline

maps = [list(map(int,input().split())) for _ in range(3)]
min_cost = float('inf')

for i in range(3):
    for height in [1,2,3]:
        cost = sum(abs(maps[i][j]-height) for j in range(3))
        min_cost = min(min_cost,cost)
for j in range(3):
    for height in [1,2,3]:
        cost = sum(abs(maps[i][j]-height) for i in range(3))
        min_cost = min(min_cost,cost)
print(min_cost)
        
