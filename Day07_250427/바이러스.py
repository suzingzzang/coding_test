# https://softeer.ai/app/assessment/index.html?xid=462529&xsrfToken=gBmXUvwbvH1P9E9b3gtLIOnpLjYjvGTz&testType=practice

import sys
input = sys.stdin.readline

k,p,n = map(int,input().split())
def pow(under,up,mod):
    result = 1
    under %= mod
    while up >0:
        if up%2 == 1:
            result = (result*under)%mod
        under = (under*under)%mod
        up //= 2
    return result

mod = 1000000007
total = pow(p,n,mod)

print((k*total)%mod)
