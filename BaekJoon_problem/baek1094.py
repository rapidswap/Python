stick=[64,32,16,8,4,2,1]

X=int(input())
sum=0
cnt=0
for i in range(len(stick)):
    cnt+=1
    sum+=stick[i]
    if sum > X:
        sum-=stick[i]
        cnt-=1
print(cnt)