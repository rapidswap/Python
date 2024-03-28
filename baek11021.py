a = int(input())
k =0
mean = []

for i in range(a):
    num1, num2 = map(int, input().split())
    mean.append(num1)
    mean.append(num2)
for j in range(a):
    print(mean[k],mean[k+1])
    k+=2






    