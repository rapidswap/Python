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

    for i in range(N,0,-1):
        if Points[i] > Point and Point > Points[i+1]:
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
        if Points[output] == Points[i]:
            if i == N-1:
                if Points[i] == Points[i+1]:
                    print(error)
                    break
                else:
                    print(ranks[i])
            else:
                print(ranks[i])
            break