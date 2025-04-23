# https://school.programmers.co.kr/learn/courses/30/lessons/43164

def solution(tickets):
    answer = []
    tickets.sort()

    visited = [False] * len(tickets)
    
    def dfs(current,depth):
        answer.append(current)
        if depth == len(tickets):
            return True
        
        for i in range(len(tickets)):
            if not visited[i] and tickets[i][0] == current:
                visited[i] = True
                if dfs(tickets[i][1],depth+1):
                    return True
                visited[i] = False
        answer.pop()
    dfs('ICN',0)
    return answer
