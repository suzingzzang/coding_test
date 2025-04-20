# https://school.programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def solution(name):
    answer = 0
    # 커서 조작 이동
    # 알파벳 바꿈
    n = len(name)
    move = n-1
    for i in range(n):
        next_idx = i+1
        while next_idx < n and name[next_idx]=='A':
            next_idx += 1
        distance = i + i + (n-next_idx)
        alt_distance = i + 2*(n-next_idx)
        move = min(move,distance,alt_distance)
    
    for i in name:
        answer += min(ord(i) -ord('A'),ord('Z') - ord(i)+1 )
    return answer + move
