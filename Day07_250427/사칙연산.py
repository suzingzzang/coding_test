# https://school.programmers.co.kr/learn/courses/30/lessons/1843

def solution(arr):
    n = (len(arr) + 1) // 2  
    numbers = [int(arr[i]) for i in range(0, len(arr), 2)]  
    operators = arr[1::2]  

    dp_max = [[0] * n for _ in range(n)]
    dp_min = [[0] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = numbers[i]
        dp_min[i][i] = numbers[i]


    for length in range(2, n + 1): 
        for i in range(n - length + 1):
            j = i + length - 1  


            dp_max[i][j] = -float('inf')
            dp_min[i][j] = float('inf')

            for k in range(i, j):
                if operators[k] == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k + 1][j])
                elif operators[k] == '-':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k + 1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k + 1][j])

    return dp_max[0][n - 1]
