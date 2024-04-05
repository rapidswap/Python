A,B=map(int, input().split())
minmul=1

while True:
    found=False
    for i in range(2, min(A, B)+1):
        if A % i == 0 and B % i == 0:
            A = A//i
            B = B//i
            minmul *= i
            found=True
            break
    if not found:
        break
            
minmul= minmul * A * B

print(int(minmul))