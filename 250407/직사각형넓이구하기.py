#https://school.programmers.co.kr/learn/courses/30/lessons/120860
def solution(dots):
    answer = 0
    index_list = []
    ver = 0
    hor = 0
    for i in range(len(dots)):
        for j in range(2):
            answer += dots[i][j]
            
        index_list.append(answer)
        answer = 0
    
    index = index_list.index(max(index_list))
    for a in range(len(dots)):
        for b in range(2):
            if dots[a][b] == dots[index][0]:
                ver = dots[index][1] -dots[a][b] 
                print(dots[index][0],1111111111,dots[a][b])
            elif dots[a][b] == dots[index][1]:
                hor = dots[index][0] - dots[a][b]
    
    return ver * hor

###############################################################쉽게생각하자....수학적사고능력을 기르자...
def solution(dots) :
	return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])
