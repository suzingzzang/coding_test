# https://school.programmers.co.kr/learn/courses/30/lessons/42898

def solution(m, n, puddles):
    answer = 0
    dp = [[0]*(m+1) for _ in range(n+1)]
    dp[1][1] = 1
    for x , y in puddles:
        dp[y][x] = -1
        
    for i in range(1,n+1):
        for j in range(1,m+1):
            if dp[i][j] == -1:
                dp[i][j] =0
                continue
            if i > 1:
                dp[i][j] += dp[i-1][j]
            if j > 1:
                dp[i][j] += dp[i][j-1]
            dp[i][j] %= 1000000007
    return dp[n][m]
