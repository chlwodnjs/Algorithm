from collections import deque


def bfs(x,y):
    q.append((x,y))
    while q:
        x1,y1 = q.popleft()
        if not graph[x1][y1]:
            graph[x1][y1] = 1
            for k in range(4):
                nx = x1+dx[k]
                ny = y1+dy[k]
                if 0<=nx<N and 0<=ny<N and RGB[nx][ny]==RGB[x1][y1]:
                    q.append((nx,ny))

if __name__ == '__main__':
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    q=deque()
    check_rgb = 0
    check_rb = 0

    N = int(input())
    RGB = [(list(map(str,input()))) for _ in range(N)]
    graph = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not graph[i][j]:
                bfs(i,j)
                check_rgb+=1

    graph = [[0]*N for _ in range(N)]
    for n in range(N):
        for m in range(N):
            if RGB[n][m]!='B':
                RGB[n][m]='R'
    for n in range(N):
        for m in range(N):
            if not graph[n][m]:
                bfs(n,m)
                check_rb+=1

    print(check_rgb, check_rb)

