# https://www.acmicpc.net/problem/31246

import sys
input = sys.stdin.readline

N , K = map(int, input().split())

ad_list = [tuple(map(int,input().split())) for _ in range(N)]

def win(x):
    count = 0
    for a,b in ad_list:
        if a+x >= b:
            count += 1
    return count >= K

low = 0
high = 10**9
answer = 0
while low <= high:
    mid = (low + high) //2
    if win(mid):
        answer = mid
        high = mid-1
    else:
        low = mid+1

print(answer)
