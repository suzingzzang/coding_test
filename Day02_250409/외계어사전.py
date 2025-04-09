# https://school.programmers.co.kr/learn/courses/30/lessons/120869
# set() 집합 자료형 / 중복 x / 순서 x
# s2 = set("Hello")
# s2
# {'e', 'H', 'l', 'o'}
def solution(spell, dic):
    answer = 0
    spell = set(spell)
    for i in dic:
        if not spell - set(i):
            return 1
    return 2

