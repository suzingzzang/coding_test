# https://www.acmicpc.net/problem/1919
import sys 
input = sys.stdin.readline

A = input().strip()
B = input().strip()
alpha = 'abcdefghijklmnopqrstuvwxyz'
dict = {}
for i in alpha:
    dict[i] = 0
for a in A:
    dict[a] += 1
for b in B:
    dict[b] -= 1
result = 0
for j in dict:
    result += abs(dict[j])

print(result)
