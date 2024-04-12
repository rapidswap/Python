w0 = -1.5
w1 = 1
w2 = 1
learning_rate = 0.1  # 학습률

def ANDGATE(x1, x2):
    global w0, w1, w2
    output = w1 * x1 + w2 * x2 + w0 * 1  # x0를 1로 대체
    if output >= 0.5:
        y = 1
    else:
        y = 0
    delta = y - (x1 and x2)  # 기대 출력과 실제 출력 사이의 차이
    w1 -= learning_rate * delta * x1  # 델타 규칙을 사용하여 가중치 업데이트
    w2 -= learning_rate * delta * x2
    w0 -= learning_rate * delta * 1  # x0는 항상 1이므로 여기서는 직접 처리
    print(x1, end="\t")
    print(x2, end="\t")
    if output < 0:
        print(output, end="\t")
    else:
        print("", output, end="\t")
    print(y, end="\t")
    print()


print("x1      x2       W.X    y")
for _ in range(20):  # 학습 반복 횟수
    for i in range(2):
        for j in range(2):
            ANDGATE(i, j)
