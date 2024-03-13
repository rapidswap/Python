
print("행과 열을 먼저 입력합니다.")
rows1=int(input("첫 번째 행: "))
cols1=int(input("첫 번째 열: "))
mult1 = [[0] * cols1 for _ in range(rows1)]
for i in range(rows1):
    for j in range(cols1):
        mult1[i][j] = int(input("[{}] [{}] 숫자: ".format(i, j)))
        
rows2=int(input("두 번째 행: "))
cols2=int(input("두 번째 열: "))
mult2 = [[0] * cols2 for _ in range(rows2)]
for i in range(rows2):
    for j in range(cols2):
        mult2[i][j]=int(input("[{}] [{}] 숫자: ".format(i, j)))
#mult1=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
#mult2=[[1,2],[3,4],[5,6],[7,8]]
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


