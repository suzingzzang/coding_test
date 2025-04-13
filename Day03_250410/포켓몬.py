# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):

    unique_types = list(set(nums))
    num_unique_types = len(unique_types) 
    print(unique_types)
    
    # 최대 선택 가능한 포켓몬
    max_select = len(nums) // 2
    
    # 고유 포켓몬의 수와 선택 가능한 포켓몬 수를 비교하여 결과를 반환
    
    #1. 고유 > 최대 선택: return 최대 선택
    if num_unique_types > max_select: 
        return max_select
    #2. 고유 < 최대: return 고유
    else:
        return num_unique_types
