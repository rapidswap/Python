create_num=[]
CN=False
for i in range(1, 10000):
    if i // 10 == 0:
        create_num.append(int(i+i))
    elif i // 100 == 0:
        create_num.append(int(i+i//10+i%10))
    elif i // 1000 == 0:
        create_num.append(int(i+i//100+(i%100//10)+i%10))
    elif i // 10000 == 0:
        create_num.append(int(i+i//1000+(i%1000//100)+(i%100//10)+i%10))

for i in range(1,10000):
    for j in create_num:
        if j == i:
            CN=True
            break
    if CN == True:
        CN = False
        continue
    else:
        print(i)
        