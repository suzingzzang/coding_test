def solution(price, money, count):
    sum_cnt = 0
    for i in range(1,count+1):
        sum_cnt += price * i 

    return sum_cnt-money if (sum_cnt-money) > 0 else  0
