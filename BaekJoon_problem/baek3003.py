# 1 1 2 2 2 8
white_chess=[]
white=[1,1,2,2,2,8]
need_white=[0,0,0,0,0,0]

pieces_input = input()
white_chess = list(map(int, pieces_input.split()))

for j in range(len(range(len(white)))):
    if white[j] !=need_white[j]:
        need_white[j]=int(white[j])-int(white_chess[j])
print(need_white[0],need_white[1],need_white[2],need_white[3],need_white[4],need_white[5])
