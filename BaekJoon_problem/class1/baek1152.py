N = input()
cnt=1 
for i in range(len(N)):
    if len(N) == 1:
        if N[i] == ' ':
            cnt=0
            break
    if N[i] == ' ':
        if i == 0 or i == len(N)-1:
            continue
        cnt+=1
print(cnt) 