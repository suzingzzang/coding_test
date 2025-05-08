# https://www.acmicpc.net/problem/26091
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
members = list(map(int,input().split()))
low = 0
high = N-1
members.sort()
count= 0
while low < high:
    if members[low] + members[high] >= M:
        count+=1
        low += 1
        high -= 1

    else:
        low += 1
print(count)
