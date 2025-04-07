#https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    answer = 0
    danger_x = [-1,-1,-1,0,0,1,1,1]
    danger_y = [-1,0,1,-1,1,-1,0,1]
    box = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                box.append((i,j))
    for x , y in box:
        for k in range(len(danger_x)):
            nx = x+danger_x[k]
            ny = y+danger_y[k]
            if 0 <= nx < len(board) and 0 <= ny < len(board):
                board[nx][ny] = 1
    for a in board:
        answer += a.count(0)        
        
    return answer
