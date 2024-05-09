N= int(input())
Num=[[0]*2 for i in range(N)]
for i in range(N):
    Num[i]=list(map(int,input().split()))

Num.sort()    


for i in range(N):
    print(Num[i][0],Num[i][1])