# https://softeer.ai/app/assessment/index.html?xid=459244&xsrfToken=U1mq36ShKyMgjtQO0322AkdgQyB6KtVa&testType=practice

import sys
input = sys.stdin.readline

N = int(input())
numbers = [input().strip() for _ in range(N)]
def solution(i):
    if '.' in i:
        x , y = i.split('.')
        return (int(x),int(y),1)
    else:
        x = int(i)
        return (x , -1 ,0)
numbers.sort(key=lambda x : solution(x))

for i in numbers:
    print(i)
