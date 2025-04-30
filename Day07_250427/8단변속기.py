# https://softeer.ai/app/assessment/index.html?xid=462545&xsrfToken=ZcnPNsD01PTQyabI0iinw5rPlGGqriLH&testType=practice

import sys
input = sys.stdin.readline

maps = list(map(int,input().split()))
if maps == list(range(1,9)):
    print('ascending')
elif maps == list(range(8,0,-1)):
    print('descending')
else:
    print('mixed')
    
