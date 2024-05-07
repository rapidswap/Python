N,K = map(int, input().split())

people=[]
kill=[]
cnt=0
for i in range(1,N+1):
    people.append(i)


while True:
    if len(people) == 0:
        break
    for i in range(K):
        if cnt > len(people) - 1:
            cnt=0
            if i == K-1:
                kill.append(people[cnt])
                people.remove(people[cnt])
                cnt=0
                break
        elif i == K-1:
            kill.append(people[cnt])
            people.remove(people[cnt])
            cnt-=1
        cnt+=1
print("<",end="")
for i in range(len(kill)):
    if i == len(kill)-1:
        print(kill[i],end=">")  
        break      
    print(kill[i],end=", ")
        