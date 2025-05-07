#https://www.acmicpc.net/problem/31090

import sys
input = sys.stdin.readline

T = int(input())
test_case = [int(input()) for _ in range(T)]


for i in test_case:
    div = i % 100


    if (i+1) % div == 0:
        print('Good')
    else:
        print('Bye')
