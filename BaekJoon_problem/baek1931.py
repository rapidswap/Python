num = int(input())
room = []

for i in range(num):
    start_time, end_time = map(int, input().split())
    room.append((start_time, end_time))

room.sort()  # 시작 시간을 기준으로 정렬

cnt = 0
end_time = 0

for start_time, new_end_time in room:
    if start_time >= end_time:  # 새로운 회의 시작 시간이 이전 회의 종료 시간보다 크거나 같을 때
        end_time = new_end_time
        cnt += 1
    elif new_end_time < end_time:  # 이전 회의 종료 시간보다 새로운 회의 종료 시간이 작을 때
        end_time = new_end_time


print(cnt)