# https://www.acmicpc.net/problem/27376

import sys
input = sys.stdin.readline

n,k = map(int,input().split())
sign_list = [list(map(int,input().split())) for _ in range(k)]
sign_list.sort()
cur_time = 0
cur_pos = 0
for x,t,s in sign_list:
    cur_time += (x - cur_pos)
    cur_pos = x

    if cur_time < s:
        cur_time += (s - cur_time)
    else:
        cycle = 2*t
        first_green = (cur_time - s) % cycle
        if first_green >=t:
            cur_time += (cycle - first_green)
cur_time += n - cur_pos
print(cur_time)
