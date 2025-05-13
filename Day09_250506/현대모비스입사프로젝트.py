# https://www.acmicpc.net/problem/27922

import sys
input = sys.stdin.readline

N,K = map(int,input().split())
study_list = [tuple(map(int,input().split())) for _ in range(N)]
max_sum = 0
for i , j in [(0,1),(0,2),(1,2)]:
    max_lecture = [study[i] + study[j] for study in study_list]
    max_lecture.sort(reverse=True)
    max_sum = max(max_sum , sum(max_lecture[:K]))
print(max_sum)
