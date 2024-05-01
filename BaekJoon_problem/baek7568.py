N = int(input())

human=[[0]*2]*N
cnt=0
rank=1
ranklist=[]

for i in range(N):
    human[i] = list(map(int, input().split()))

for i in range(N):
    human_com=human[i]
    for j in range(N):
        if j == cnt:
            continue
        else:
            if human_com[0] < human[j][0] and human_com[1] < human[j][1]:
                rank+=1
    ranklist.append(rank)
    rank=1
    cnt+=1

for i in range(N):
    print(ranklist[i],end=" ")

                
