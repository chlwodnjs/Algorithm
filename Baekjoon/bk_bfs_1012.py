from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<N and 0<=ny<M and graph[nx][ny]!=0:
                graph[nx][ny] = 0
                q.append((nx, ny))


if __name__ == '__main__':
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]
    q=deque()
    for i in range(int(input())):
        check=0
        N,M,K = map(int,input().split())
        graph = [[0]*M for _ in range(N)]

        for j in range(K):
            bae,chu = map(int,input().split())
            graph[bae][chu]=1

        for ba in range(N):
            for ch in range(M):
                if graph[ba][ch]==1:
                    check += 1
                    q.append((ba,ch))
                    graph[ba][ch] = 0
                    bfs()
        print(check)
