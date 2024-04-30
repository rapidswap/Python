N = int(input())
if N % 2 == 0 :
    exit()
Candy=[]
Com_Candy=[]
cnt=0

for i in range(N):
    A = input()
    Candy.append(int(A))

first_Candy=0

for vlaue in Candy:
    if cnt % 2 == 0:
        first_Candy += vlaue
    else:
        first_Candy -= vlaue
    cnt+=1
        
Com_Candy.append(first_Candy//2)

for i in range(N-1):
    Com_Candy.append(Candy[i] - Com_Candy[i])

for i in Com_Candy:
    print(i)
