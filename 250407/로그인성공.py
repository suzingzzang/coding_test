# https://school.programmers.co.kr/learn/courses/30/lessons/120883
def solution(id_pw, db):
    answer = ''
    for j in range(len(db)):
        if id_pw[0] == db[j][0] and id_pw[1] == db[j][1]:
            return 'login'
        elif id_pw[0] == db[j][0] and id_pw[1] != db[j][1]:
            return 'wrong pw'
        elif id_pw[0] != db[j][0] and id_pw[1] != db[j][1]:
            return 'fail'
                    
############################################################### 재도전
def solution(id_pw, db):
    answer = ''
    for j in range(len(db)):
        if id_pw[0] == db[j][0] and id_pw[1] == db[j][1]:
            answer = 'login'
        elif id_pw[0] == db[j][0] and id_pw[1] != db[j][1]:
            answer = 'wrong pw'
        elif id_pw[0] != db[j][0] and id_pw[1] != db[j][1]:
            answer = 'fail'
    return answer
