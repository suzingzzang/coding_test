def cal_time(s):
    s = int(s.replace(':',''))
    h = s//100
    m = s%100
    return h*60 +m
def string_time(i):
    h = i //60
    m = i %60
    return f'{h:02}' +':'+ f'{m:02}'
def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    int_video = cal_time(video_len)
    int_pos = cal_time(pos)
    int_start = cal_time(op_start)
    int_end = cal_time(op_end)
    for i in commands:
        print(i)
        #오프닝 스킵
        if int_start <= int_pos <= int_end:

            int_pos = int_end
            
        #앞으로
        if i == 'next':
            if int_pos + 10 >= int_video:
                int_pos = int_video
            else : int_pos += 10
            
        #뒤로
        elif i == 'prev':

            if int_pos - 10 <= 0 :
                int_pos = 0
            else : int_pos -= 10 
    if int_start <= int_pos <= int_end:
        int_pos = int_end
    answer = string_time(int_pos)  
    return answer
