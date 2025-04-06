def solution(n):
    answer = ''
    n_list = ['1','2','4']
    while n > 0 :
        n = n-1
        answer = n_list[n%3] + answer
        n //= 3  # 왜 필요한지 조금 더 생각해보기
    return answer
