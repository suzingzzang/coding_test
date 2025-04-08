from collections import deque
def solution(ingredient):
    answer = 0
    temp_list = []
    for i in ingredient:
        temp_list.append(i)

        if len(temp_list) >=4:
            bread1 = temp_list[len(temp_list)-4]
            veg = temp_list[len(temp_list)-3]
            meat = temp_list[len(temp_list)-2]
            bread2 = temp_list[len(temp_list)-1]

            if bread1 == 1 and veg == 2 and meat == 3 and bread2 == 1:
                temp_list.pop()
                temp_list.pop()
                temp_list.pop()
                temp_list.pop()
                answer += 1


    return answer
