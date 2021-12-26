from collections import deque
import sys

def bfs():

    while q:
        z,x,y = q.popleft()

        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]
            if 0<=nx<N and 0<=ny<M and 0<=nz<H and graph[nz][nx][ny]==0:
                graph[nz][nx][ny]=graph[z][x][y]+1
                q.append((nz,nx,ny))

if __name__=='__main__':
    dx=[1,0,-1,0,0,0]
    dy=[0,1,0,-1,0,0]
    dz=[0,0,0,0,1,-1]

    q = deque()
    check=-1

    M,N,H = map(int,input().split())

    graph = [[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]

    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m] == 1 :
                    q.append((h,n,m))
    bfs()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if graph[h][n][m]==0:
                    print(-1)
                    sys.exit(0)
                    # quit()
                check = max(check,graph[h][n][m])
    if check==1:
        print(0)
    else:
        print(check-1)