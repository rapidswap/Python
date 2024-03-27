now_time=list(map(int, input("현재 시각 입력: ").split()))
set_time=int(input("진행 시간 입력: "))

now_time[1] += set_time

if now_time[1] >= 60:
    while(True):
        now_time[1] = now_time[1] - 60
        now_time[0] += 1
        if now_time[1] < 60:
            break

if now_time[0] >= 24:
    now_time[0] -= 24
    
print(now_time[0], now_time[1])