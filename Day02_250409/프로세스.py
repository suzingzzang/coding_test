# https://school.programmers.co.kr/learn/courses/30/lessons/42587#

def solution(priorities, location):
    answer = 0
    que = []
    
    for i in enumerate(priorities):
        que.append(i)
    
    execute_order = 0
    while True:
        # 큐에서 첫 번째 프로세스 꺼내기
        current = que.pop(0)
        
        # 우선순위가 더 높은 프로세스가 있는지 확인
        higher_priority_exists = False
        for other in que:
            if current[1] < other[1]:
                higher_priority_exists = True
                break
        
        if higher_priority_exists:
            # 더 높은 우선순위가 있으면, 현재 프로세스를 다시 큐에 넣음
            que.append(current)
        else:
            # 그렇지 않으면, 현재 프로세스를 실행
            execute_order += 1
            
            # 만약 현재 프로세스가 우리가 찾는 프로세스라면 실행 순서를 반환
            if current[0] == location:
                return execute_order
