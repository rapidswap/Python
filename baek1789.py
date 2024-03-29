cnt=0
num=int(input())
sum=0
for i in range(1,num+1):
    sum+=i
    if sum > num:
        break
    cnt+=1

print(cnt)