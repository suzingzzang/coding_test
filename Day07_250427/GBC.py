# https://softeer.ai/app/assessment/index.html?xid=462744&xsrfToken=nQhPYTFGOcAASUdsdWO19knetPQmEYWP&testType=practice

import sys
input = sys.stdin.readline

N , M = map(int,input().split())
limit_list = []
test_list = []

for _ in range(N):
    length, speed = map(int,input().split())
    limit_list.extend([speed] * length)
for _ in range(M):
    length, speed = map(int,input().split())
    test_list.extend([speed] * length)

max_over = 0
for i in range(100):
    over = test_list[i] - limit_list[i]
    if max_over < over:
        max_over = over

print(max_over)
