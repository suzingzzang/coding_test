#  https://softeer.ai/app/assessment/index.html?xid=462227&xsrfToken=44x6mv8Ijdpd4mdF7h8UhNSsQH0iX134&testType=practice

import sys
input = sys.stdin.readline

S = input().strip()
S = S.replace('()','(1)').replace(')(',')+(')
print(S)
