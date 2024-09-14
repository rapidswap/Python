import sys

input = sys.stdin.readline
n,m = map(int, input().split())

map = [list(map(int, input().split()))for _ in range(n)]

chk=[[False]*m for _ in range(n)]


dy = [1,0,0,-1]
dx = [0,1,-1,0]
def bfs(y,x):
    rs=1
    q=[(y,x)]
    while q:
        oy,ox=q.pop()
        for k in range(4):
            ny = oy + dy[k]
            nx = ox + dx[k]
            if 0<=ny<n and 0<=nx<m:
                if chk[ny][nx]==False and map[ny][nx] ==1:
                    rs+=1
                    chk[ny][nx] = True
                    q.append((ny,nx))
    return rs


cnt = 0
maxv = 0
for i in range(n):
    for j in range(m):
        if map[i][j] == 1 and chk[i][j] == False:
            chk[i][j] = True
            cnt += 1
            maxv = max(maxv, bfs(i,j))

print(cnt)
print(maxv)