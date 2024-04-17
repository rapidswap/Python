#OR Gate perceptron
w0 = -0.5
w1 = 1
w2 = 1
learning_rate = 0.01  # 학습률

def feedforward(x1, x2):
    global w0, w1, w2
    output = w1 * x1 + w2 * x2 + w0 * 1  # x0를 1로 대체
    if output > 0:
        return 1, output  # 출력값과 임계값 이전의 출력값 반환
    else:
        return 0, output

def compute_error(target, predicted):
    return target - predicted

def weight_update(x1, x2, error):
    global w0, w1, w2
    w1 += learning_rate * error * x1
    w2 += learning_rate * error * x2
    w0 += learning_rate * error * 1  # x0는 항상 1이므로 여기서는 직접 처리

def train_OR_gate():
    print("x1\t x2\t W.X\t y\t Output before threshold")
    for _ in range(100):  # 학습 반복 횟수
        for i in range(2):
            for j in range(2):
                x1, x2 = i, j
                target = x1 or x2
                predicted, output_before_threshold = feedforward(x1, x2)
                error = compute_error(target, predicted)
                weight_update(x1, x2, error)
                print(f"{x1}\t {x2}\t", end="")
                if predicted < 0.5:
                    print("", predicted, end="\t")
                else:
                    print(predicted, end="\t")
                print(target, end="\t")
                print(output_before_threshold)

train_OR_gate()

def test_OR_gate():
    test_pattern = [(0, 0), (0, 0.3), (0, 0.5), (0, 0.8), (0, 1), (0.3, 0), (0.5, 0), (0.8, 0), (1, 0), (1, 1)]
    print("Test Pattern\tPredicted Output\t\tnet")
    for pattern in test_pattern:
        x1, x2 = pattern
        target = x1 or x2
        predicted, outnet = feedforward(x1, x2)  # 출력값 이전의 출력값은 필요 없으므로 "_"로 받습니다.
        outnet_formatted = "{:.2f}".format(outnet)  # 소수점 두 자리까지 형식화
        error = compute_error(target, predicted)
        pattern_str = f"({x1}, {x2}):"
        print(f"{pattern_str:<15} {predicted:<18} \t\t{outnet_formatted}")
        
test_OR_gate()
