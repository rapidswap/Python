import numpy as np
 
A=np.array([[0,1,1,0],
            [0,1,1,0],
            [0,1,1,0],
            [0,1,1,0]])
B=np.array([[0,0,0,0],
            [1,1,1,1],
            [1,1,1,1],
            [0,0,0,0]])
C=np.array([[0,1,1,0],
            [0,1,1,0],
            [0,0,1,1],
            [0,1,1,0]])
def dist(A,B,row,cols):
    tmp=0
    for i in range(row):
        for j in range(cols):
            tmp += np.power((A[i][j]-B[i][j]),2)
    return tmp
D=dist(A,B,4,4)
E=dist(B,C,4,4)
F=dist(A,C,4,4)
print(D)
print(E)
print(F)
 
