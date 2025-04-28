# https://school.programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    def circle(money):
        n = len(money) 
        dp = [0]*n
        dp[0] = money[0]
        dp[1] = max(money[0],money[1])
        for i in range(2,n):
            dp[i] = max(dp[i-1] , dp[i-2]+ money[i])
        return dp[-1]
        
    case1 = circle(money[:-1])
    case2 = circle(money[1:])
    return max(case1,case2)
