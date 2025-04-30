# https://softeer.ai/app/assessment/index.html?xid=462519&xsrfToken=ZThCTnCxXMpbZJuOJWWAECrWdbEvFo66&testType=practice

import sys
from collections import deque
input = sys.stdin.readline

w,n = map(int,input().split())
gold_list = [list(map(int,input().split())) for _ in range(n)]
gold_list.sort(key = lambda x: x[1], reverse=True)
result = 0
for m ,p in gold_list:
    if w == 0:
        break
    cost = min(m,w)
    result += p*cost
    w -= cost
print(result)
    
    
