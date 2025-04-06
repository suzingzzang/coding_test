def cal(diffs,times,limit,level):
    time = 0
    for i in range(len(diffs)):
        if diffs[i] <= level:
            time += times[i]
        elif diffs[i] > level:
            time += ((diffs[i]-level)*(times[i] + times[i-1])) + times[i] 
        if time > limit: return False
    return True

def solution(diffs, times, limit):
    answer = 0
    lv_min = min(diffs)
    lv_max = max(diffs)

    while lv_min <= lv_max:
        lv_mid = (lv_min + lv_max) // 2
        if cal(diffs,times,limit,lv_mid):
            answer = lv_mid
            lv_max = lv_mid-1        
        else:
            lv_min = lv_mid +1
            

            

    
    return answer
