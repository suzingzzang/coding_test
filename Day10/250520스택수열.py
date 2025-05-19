# https://www.acmicpc.net/problem/1874

import sys
input = sys.stdin.readline
n = int(input())
nums = [int(input()) for _ in range(n)]

current = 1
stack = []
result = []
possible = True
for num in nums:
    while current <= num :
        stack.append(current)
        result.append('+')
        current += 1
        
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        possible = False
        break
if possible:
    for r in result:
        print(r)
else: print('NO')
