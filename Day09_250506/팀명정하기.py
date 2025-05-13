# https://www.acmicpc.net/problem/28114

import sys
input = sys.stdin.readline

imfor_list = [list(map(str,input().split())) for _ in range(3)]
list_1 = sorted(imfor_list,key = lambda x: x[1])

print(''.join(list_1[i][1][2:] for i in range(3)))

list_2 = sorted(imfor_list,key = lambda x: -int(x[0]))

print(''.join(list_2[i][2][:1] for i in range(3)))
