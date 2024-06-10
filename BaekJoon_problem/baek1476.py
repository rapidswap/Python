E,S,M=list(map(int,input().split()))
check=0
for i in range(10000):
    check=28*i+S
    if check%15 == E and check%28 == S and check%19 == M:
        print(check)
        break
    elif E == 15 and S == 28 and M == 19:
        if check % 15 == 0 and check % 28 == 0 and check % 19 == 0:
            print(check)
            break
    elif E == 15 and S == 28:
        if check % 15 == 0 and check % 28 == 0 and check % 19 == M:
            print(check)
            break
    elif E==15 and M == 19:
        if check % 15 == 0 and check % 19 == 0 and check % 28 == S:
                print(check)
                break
    elif S==28 and M == 19:
        if check % 15 == E and check % 19 == 0 and check % 28 == 0:
                print(check)
                break
    elif E == 15:
         if check % 15 == 0 and check % 19 == M and check % 28 == S:
                print(check)
                break
    elif M == 19:
         if check % 15 == E and check % 19 == 0 and check % 28 == S:
                print(check)
                break
    elif S == 28:
        if check % 15 == E and check % 19 == M and check % 28 == 0:
            print(check)
            break
