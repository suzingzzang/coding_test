# https://school.programmers.co.kr/learn/courses/30/lessons/42628

import heapq
def solution(operations):
    answer = []
    heap = []
    for i in operations:
        num = int(i.split(' ')[1])
        if 'I' in i:
            heapq.heappush(heap,num)            
        elif 'D' in i:
            if heap:
                if num == -1:
                    heapq.heappop(heap)
                elif num == 1:
                    heap.pop()

                
    if heap:
        return [heapq.nlargest(1,heap)[0],heap[0]]
    else:
        return [0,0]
######################################################################    min_heap / max_heap 으로도 풀기 
import heapq
def solution(operations):
    answer = []
    heap = []
    for i in operations:
        num = int(i.split(' ')[1])
        if 'I' in i:
            heapq.heappush(heap,num)            
        elif 'D' in i:
            if heap:
                if num == -1:
                    heapq.heappop(heap)
                elif num == 1:
                    heap.remove(heapq.nlargest(1,heap)[0])

                
    if heap:
        return [heapq.nlargest(1,heap)[0],heap[0]]
    else:
        return [0,0]
