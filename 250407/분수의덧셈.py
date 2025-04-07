# https://school.programmers.co.kr/learn/courses/30/lessons/120808
# gcd 최대공약수 lcm 최소공배수
import math
def solution(numer1, denom1, numer2, denom2):
    denom = denom1 * denom2
    numer = numer1*denom2 + numer2*denom1
    answer = math.gcd(denom,numer)

    return [numer/answer , denom/answer]
