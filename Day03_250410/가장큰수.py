# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    numbers = [str(x) for x in numbers]

    numbers.sort(key=lambda x: x*3, reverse=True)

    answer = str(int(''.join(numbers)))

    return answer
