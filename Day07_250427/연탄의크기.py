# https://softeer.ai/app/assessment/index.html?xid=462419&xsrfToken=Aa7kriT4TL6WxK8CqWOzrbxX3nKj66YC&testType=practice

import sys,math
input = sys.stdin.readline

n = int(input())
r_list = list(map(int, input().split()))
r_list.sort()
result = 0
for i in range(n):
    for j in range(i+1,n):
        gcd_list = math.gcd(r_list[i],r_list[j])

        tmp_count = sum(1 for r in r_list if gcd_list != 1 and r % gcd_list == 0)

        result = max(result,tmp_count)
if result == 0:
    print(1)
else: print(result)
    
