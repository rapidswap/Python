mult1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
mult2=[[1,2],[3,4],[5,6],[7,8]]
tmpmult=[]
matrixnum=0

if len(mult1[0]) == len(mult2):
    newmult = [[0] * len(mult2[0]) for _ in range(len(mult1))]
    
    for n in range(len(mult2[0])):
        for i in range(len(mult1)):
            for j in range(len(mult1[0])):
                matrixnum = matrixnum + (mult1[i][j] * mult2[j][n])
                if j == 3:
                    newmult[i][n]=matrixnum
                    matrixnum=0
        
print(newmult)


