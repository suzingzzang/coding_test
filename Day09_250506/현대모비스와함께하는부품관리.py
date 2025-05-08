# https://www.acmicpc.net/problem/24724
import sys
input = sys.stdin.readline
T = int(input())
for t in range(T):
    N = int(input())
    A, B = map(int, input().split())
    for _ in range(N):
        input()  
    print(f'Material Management {t+1}')
    print('Classification ---- End!')
