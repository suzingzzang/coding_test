# https://school.programmers.co.kr/learn/courses/30/lessons/120878

import math
def solution(a, b):
    answer = 0
    b = b/math.gcd(a,b)
    if a > b and a %b == 0:
        return 1
    if b % 2 == 0 or b %5 == 0:
        if b %3 == 0:
            return 2
        return 1
    else:
        return 2
