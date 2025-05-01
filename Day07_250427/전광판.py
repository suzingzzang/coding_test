# https://softeer.ai/app/assessment/index.html?xid=462753&xsrfToken=sXYovStWGpAZiGQ2fGBzJrZvLV2mCyAt&testType=practice

import sys
input = sys.stdin.readline
T = int(input())
light_list = [
    [1,1,1,0,1,1,1], #0
    [0,0,1,0,0,1,0], #1
    [1,0,1,1,1,0,1], #2
    [1,0,1,1,0,1,1], #3
    [0,1,1,1,0,1,0], #4
    [1,1,0,1,0,1,1], #5
    [1,1,0,1,1,1,1], #6
    [1,1,1,0,0,1,0], #7
    [1,1,1,1,1,1,1], #8
    [1,1,1,1,0,1,1]  #9
]
off_light = [0, 0, 0, 0, 0, 0, 0]

for _ in range(T):
    a_str, b_str = input().strip().split()
    n_a = len(a_str)
    n_b = len(b_str)

    count = 0
    for i in range(5):
        light_a = off_light
        light_b = off_light

        if i < n_a:
            digit_a = int(a_str[n_a - 1 - i])
            light_a = light_list[digit_a]

        if i < n_b:
            digit_b = int(b_str[n_b - 1 - i])
            light_b = light_list[digit_b]

        for j in range(7):
            if light_a[j] != light_b[j]:
                count += 1

    print(count)
