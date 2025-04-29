# https://softeer.ai/app/assessment/index.html?xid=462390&xsrfToken=eBV5aQiY0OCSfcmTjGxGJoqaavToqwBv&testType=practice

import sys
input = sys.stdin.readline

N = int(input())
str_list = [input().split() for _ in range(N)]
result = []

for i in range(N):
    left,right = str_list[i]  

    idx = left.lower().find('x')  
    ch = right[idx]

    if ch.islower():
        ch = ch.upper()

    result.append(ch)

print(''.join(result))
