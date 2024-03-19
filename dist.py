import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[10,11,12],[13,14,15],[16,17,18]])
def dist(A,B,row,cols):
    tmp=0
    for i in range(row):
        for j in range(cols):
            tmp += np.power((A[i][j]-B[i][j]),2)
    return tmp
C=dist(A,B,3,3)
print(C)
