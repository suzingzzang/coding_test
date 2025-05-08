# https://www.acmicpc.net/problem/25558
import sys
input = sys.stdin.readline
N = int(input())
x1,y1,x2,y2 = map(int,input().split())
min_dist = float('inf')
min_index = -1
for i in range(1,N+1):
    m = int(input())
    path = [tuple(map(int,input().split())) for _ in range(m)]

    total = 0
    cx, cy = x1,y1
    for px,py in path:
        total += abs(cx-px) + abs(cy-py)
        cx ,cy = px,py
    total  += abs(cx-x2) + abs(cy-y2)

    if total < min_dist:
        min_dist = total
        min_index = i
print(min_index)

