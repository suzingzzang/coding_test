# https://school.programmers.co.kr/learn/courses/30/lessons/120876
# set() $ 교집합 \ 합집합
def solution(lines):
    
    set1 = set()
    set2 = set()
    set3 = set()
    
    for i in range(lines[0][0], lines[0][1]):
        set1.add(i)
        
    for i in range(lines[1][0], lines[1][1]):
        set2.add(i)
        
    for i in range(lines[2][0], lines[2][1]):
        set3.add(i)

    return len((set1 & set2) | (set2 & set3) | (set1 & set3))

