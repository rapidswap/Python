N,Point,P=map(int,input().split())
error=-1
if N == 0:
    Points=Point
    if 0 == P:
        print(error)
    else:
        print("1")
else:
    Points=list(map(int, input().split()))
    def ranking(scores):
        ranked = sorted(scores, reverse=True)
        return [ranked.index(score) + 1 for score in scores]
    if N == 1:
        if Points[0] > Point:
            Points.insert(N,Point)
            output=N

        elif Points[0] < Point:
            output=0
            Points.insert(0,Point)

        elif Point == Points[0]:
            Points.insert(N,Point)
            output=N
    else:
        for i in range(N-1,0,-1):
            if Points[i] > Point:
                Points.insert(i+1,Point)
                output=i+1
                break
            elif Points[i] < Point:
                output=i
                Points.insert(i,Point)
                break
            elif Point == Points[i]:
                Points.insert(i,Point)
                output=i+1
                break

    ranks=ranking(Points)
    for i in range(P):
        if output > P-1:
            print(error)
            break
        else:
            print(ranks[output])
            break