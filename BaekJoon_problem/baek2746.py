n=int(input())
money=[]

for i in range(n):
    a,b,c=map(int,input().split())
    max_num=max(a,b,c)
        
    if a == b and a == c:
        money.append(int(10000+a*1000))
    elif a == b and a != c or a == c and a != b:
        money.append(int(1000+a*100))
    elif b == c and b != a:
        money.append(int(1000+b*100))
    else:
        money.append(int(max_num*100))
maxmoney=int(money[0])
for j in range(len(money)):
    if int(maxmoney) < int(money[j]):
        maxmoney = int(money[j])
        
print(maxmoney)