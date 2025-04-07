# https://school.programmers.co.kr/learn/courses/30/lessons/120875

def slope(d1, d2):
    return (d2[1] - d1[1])/(d2[0] - d1[0])

def solution(dots):
    answer = 0
    x1 = dots[0]

    x2 = dots[1]
    x3 = dots[2]
    x4 = dots[3]
    if slope(x1,x2) == slope(x3,x4):
        return 1
    elif slope(x1,x3) == slope(x2,x4):
        return 1
    elif slope(x1,x4) == slope(x2,x3):
        return 1
    else:
        return 0
    
