# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline
n = int(input())
numbers = list(map(int,input().split()))
x = int(input())

seen = set()
count = 0
for num in numbers:
    if x -num in seen:
        count+=1
    seen.add(num)
print(count)
