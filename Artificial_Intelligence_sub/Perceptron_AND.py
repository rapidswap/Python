w0 = -1.5
x0 = 1
w1 = 1
w2 = 1

def ANDGATE(x1, x2):
    output = w1 * x1 + w2 * x2 + w0 * x0
    if output >= 0:
        y = 1
    else:
        y = 0
    return output, y

for i in range(2):
    for j in range(2):
        output, result = ANDGATE(i, j)
        print(f"Input: ({i}, {j}), Output: {output}, Result: {result}")
