# https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = 0
    #if N == number:
    #    return 1
    dp = [set() for _ in range(9)]
    for i in range(1,9):
        dp[i].add(int(str(N)*i))
        for j in range(1,i):
            for num1 in dp[j]:
                for num2 in dp[i-j]:
                    dp[i].add(num1 + num2)
                    dp[i].add(num1 - num2)
                    dp[i].add(num1 * num2)
                    if num2 != 0:
                        dp[i].add(num1 // num2)

        if number in dp[i]:
            return i
    return -1
