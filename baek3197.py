rows, cols = map(int, input().split())
lake = []

for i in range(rows):
    lake_ice = input()
    lake.append(list(lake_ice))

day = 0

while True:
    new_lake = [row[:] for row in lake]  # 현재 호수 상태를 복사하여 새 호수를 생성합니다.
    changed = False  # 변경 여부를 추적하기 위한 변수를 초기화합니다.

    for i in range(rows):
        for j in range(cols):
            if lake[i][j] == 'X':
                if i > 0 and lake[i - 1][j] == '.':
                    new_lake[i][j] = '.'
                    changed = True
                if i < rows - 1 and lake[i + 1][j] == '.':
                    new_lake[i][j] = '.'
                    changed = True
                if j > 0 and lake[i][j - 1] == '.':
                    new_lake[i][j] = '.'
                    changed = True
                if j < cols - 1 and lake[i][j + 1] == '.':
                    new_lake[i][j] = '.'
                    changed = True

    if not changed:  # 변경이 없으면 더 이상 얼음이 녹을 수 없으므로 종료합니다.
        break

    lake = new_lake  # 새 호수 상태로 업데이트합니다.
    day += 1

print(day)
