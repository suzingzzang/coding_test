# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

N = int(input())
input_list = [input().strip() for _ in range(N)]


result = []
for i in input_list:
    if i.startswith('push'):
        result.append(i.split(' ')[1])
    elif i == 'pop':
        if result:
            print(result.pop())
        else:
            print(-1)
    elif i == 'size':
        print(len(result))
    elif i == 'empty':
        if result :
            print(0)
        else:
            print(1)
    elif i == 'top':
        if result:
            print(result[-1])    
        else:
            print(-1)
