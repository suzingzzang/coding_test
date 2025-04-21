# https://school.programmers.co.kr/learn/courses/30/lessons/42883

def solution(number, k):
    answer = ''
    stack = []
    for i in number:
        while k > 0 and  stack and stack[-1] < i:
            stack.pop()
            k -= 1
            
        stack.append(i)
    
    if k>0:
        stack = stack[:-k]
    
    return ''.join(stack)
