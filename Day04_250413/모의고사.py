# https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = [0,0,0]
    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if answers[i] == first[i%5]:
            answer[0] += 1
        if answers[i] == second[i%8]:
            answer[1] +=1
        if answers[i] == third[i%10]:
            answer[2] += 1
            
    result = []
    for i in range(3):
        if answer[i] == max(answer):
            result.append(i+1)
    #result = answer.index(max(answer))
    
    return result
