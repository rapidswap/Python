#행렬 곱셈 함수
import numpy as np

A = np.array([[2,3,7],[5,2,1],[0,1,0]])
B = np.array([[1,2],[2,7],[3,0]])

def mtx_mul(A, ar, ac, B, br, bc):
    newmult = np.zeros((ar, bc))
    for i in range(ar):
        for j in range(bc):
            for k in range(ac):
                newmult[i][j] += A[i][k] * B[k][j]
    return newmult

C = mtx_mul(A, 3, 3, B, 3, 2)
print(C)