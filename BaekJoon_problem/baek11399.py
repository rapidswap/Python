N=int(input())
Time=list(map(int,input().split()))

sumTime=0
sum=0
cnt=1
Time.sort()

for i in range(N):
    for j in range(cnt):
        sumTime+=Time[j]
    sum+=sumTime
    sumTime=0
    cnt+=1
    
print(sum)