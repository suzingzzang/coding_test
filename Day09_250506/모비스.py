# https://www.acmicpc.net/problem/28074

import sys
input = sys.stdin.readline

input_string = input()
correct_string=['M','O','B','I','S']
if all(char in input_string for char in correct_string):
    print("YES")
else:
    print('NO')

