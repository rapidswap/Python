N = int(input())
Candy=[]
Com_Candy=[]
for i in range(N):
    A = input()
    Candy.append(int(A))
candy1=Candy[0]
candy2=Candy[1]

if candy1 > candy2:
    X=candy1-candy2
elif candy2 > candy1:
    X=candy2-candy1
elif candy1 == candy2:
    candy1=Candy[0]
    candy2=Candy[2]
    if candy1 > candy2:
        X=candy1-candy2
    elif candy2 > candy1:
        X=candy2-candy1
        
Com_Candy.append(int(X)
                 )
for i in range(N-1):
    Com_Candy.append(int(Candy[i]-Com_Candy[i]))

for i in range(len(Com_Candy)):
    print(Com_Candy[i])
    