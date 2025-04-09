# https://school.programmers.co.kr/learn/courses/30/lessons/120861
def solution(keyinput, board):
    answer = []
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    key = ['up','down','left','right']
    for x in range(board[0]//2):
        for y in range(board[1]//2):
            for i in keyinput:
                if nx > board[0]//2 or nx < -(board[0]//2) or ny > board[1]//2<=(board[1]//2):
                nx = x + dx[key.index(i)]
                ny = y + dy[key.index(i)]
    answer.append(nx)
    answer.append(ny)
    return answer


  #################################################### 블로그 보고 수정
  def solution(keyinput, board):
    
    x, y = 0, 0
    x_max, y_max = board[0]//2, board[1]//2
    
    for key in keyinput:
        if key == 'up' and y < y_max:
            y += 1
        elif key == 'down' and y > -y_max: 
            y -= 1
        elif key == 'right' and x < x_max:
            x +=1
        elif key == 'left' and x > -x_max:
            x -= 1
    
    return [x, y]
