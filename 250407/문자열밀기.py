#https://school.programmers.co.kr/learn/courses/30/lessons/120921

def solution(A, B):
    a = []
    b = []
    for i in range(len(A)):
        a.append(ord(A[i]))
        b.append(ord(B[i]))
    
          
    return a
###############################################################
from collections import deque

def solution(A, B):
    
    deque_A = deque(A)
    deque_B = deque(B)
    
    for i in range(len(deque_A)):
        if deque_A == deque_B:
            return i
        deque_A.rotate(1)
        
    return -1
