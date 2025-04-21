# https://school.programmers.co.kr/learn/courses/30/lessons/42861

def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x :x[2])
    parents = [i for i in range(n)]
    
    def find(x):
        if parents[x] != x :
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a,b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parents[root_b] = root_a
            return True
        return False
    
    for a , b, cost in costs:
        if union(a,b):
            answer += cost
    return answer
