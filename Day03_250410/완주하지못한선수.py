#https://school.programmers.co.kr/learn/courses/30/lessons/42576

import collections
def solution(participant, completion):
    answer = ''
    participant = collections.Counter(participant)
    completion = collections.Counter(completion)
    answer = participant - completion
    return list(answer)[0]
