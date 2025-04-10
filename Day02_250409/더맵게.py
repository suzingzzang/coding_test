# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap,i)
    while heap[0] < K :
        x1 = heapq.heappop(heap)
        x2 = heapq.heappop(heap)
        new = x1 + x2*2
        heapq.heappush(heap,new)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            return -1
    return answer
