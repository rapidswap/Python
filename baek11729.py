
#기둥은 1,2,3 
def hanoi(n,from_,sub,to_):
    if n ==1:
        # 하노이 탑이 하나 남았을때는 1 -> 3
        print(from_,to_)
        return
    #1번 기둥에 있는 n-1개의 원반을 2번으로 이동
    hanoi(n-1,from_,to_,sub)
    print(from_,to_)
    # 2번 기둥에 있는 n-1개의 원반을 3번으로 이동
    hanoi(n-1,sub,from_,to_)

n=int(input())

print(2**n-1)
hanoi(n,1,2,3)
