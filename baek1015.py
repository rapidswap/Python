N=int(input())
B=[]
org=[]
P=list(map(int, input().split()))
for t in P:
    B.append(t)
    org.append(t)
    
cnt=0
j=0

while len(P) > 0:
    min = P[0]
    for i in range(len(P)):
        if min > P[i]:
            min = P[i]

    for i in range(len(org)):
        if min == org[i]:
            B[i] = cnt
            cnt+=1
            
    for i in range(P.count(min)):
        P.remove(min)
        
for i in range(len(B)):
    print(B[i],end=" ")