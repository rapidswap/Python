number=[]
sum=0
while True:
    num=int(input())
    if num == -1:
        break
    for i in range(1,num):
        if num % i == 0:
            sum+=i
            number.append(i)
    if sum > num or sum<num :
        print("{} is NOT perfect.".format(num))
        sum=0
        number=[]
    elif sum == num:
        print(num,end=" = ")
        for i in range(len(number)):
            print(number[i], end="")
            if i < len(number) -1 :
                print(" +",end=" ")
            else:
                print()
        sum=0
        number=[]
