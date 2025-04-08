def cal_time(s):
    h = s // 100
    m = s % 100
    return h*60 + m
def solution(schedules, timelogs, startday):
    answer = 0
    for schedule in range(len(schedules)):
        cnt =0
        for i in range(7):
            if i+startday not in [6,7,13]:
                schedule_time = cal_time(schedules[schedule])
                timelogs_time = cal_time(timelogs[schedule][i])
                if schedule_time + 10 >= timelogs_time:
                    cnt += 1             
        if cnt ==5:
            answer += 1
    return answer
