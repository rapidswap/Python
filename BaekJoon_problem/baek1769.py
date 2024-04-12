a = (input(""))
sum=0
tmpsum=0
cnt=0

for i in range(len(a)):
    sum+=int(a[i])
    
if sum < 10:
    if sum == 3 or sum == 6 or sum == 9:
        print(cnt)
        print("YES")
    else:
        print(cnt)
        print("NO")
else:
    cnt+=1   
    while(True):
        cnt+=1
        for i in range(len(str(sum))):
            tmpsum+=int(str(sum)[i])
        sum=tmpsum
        tmpsum=0
        if sum < 10:
            break

    if sum == 3 or sum == 6 or sum == 9:
        print(cnt)
        print("YES")
    else:
        print(cnt)
        print("NO")