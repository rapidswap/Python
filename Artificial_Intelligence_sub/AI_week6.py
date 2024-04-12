w0=-1.5
x0=1
w1=1
w2=1

def ANDGATE(x1,x2):
    output=w1*x1+w2*x2+w0*x0
    if output>=0.5:
        y=1
    else:
        y=0
    print(x1,end="\t")
    print(x2,end="\t")
    if output < 0:
        print(output,end="\t")
    else:
        print("",output,end="\t")
    print(y,end="\t")
    print()


print("x1      x2       W.X    y")
for i in range(2):
    for j in range(2):
        ANDGATE(i,j)
