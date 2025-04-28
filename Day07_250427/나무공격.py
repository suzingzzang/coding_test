# https://softeer.ai/app/assessment/index.html?xid=462214&xsrfToken=FvStmwrssf91GcCbJVh36s5CciDWDXjK&testType=practice

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
maps = [list(map(int,input().split())) for _ in range(n)]

L1,R1 = map(int,input().split())
L2,R2 = map(int,input().split())
def attack(L,R):
    for row in range(L-1,R):
        for col in range(m):
            if maps[row][col] == 1:
                maps[row][col] = 0
                break
attack(L1,R1)
attack(L2,R2)
answer = sum(row.count(1) for row in maps)
print(answer)
