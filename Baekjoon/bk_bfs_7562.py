from collections import deque

def bfs(go):

    while q:
        x,y = q.popleft()
        if x==go[0] and y==go[1]:
            return graph[x][y]
        for k in range(8):
            nx = x+ dx[k]
            ny = y+ dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny]==0:
                    graph[nx][ny]=graph[x][y]+1
                    q.append((nx,ny))

if __name__ == '__main__':
    dx=[2,1,-1,-2,-2,-1,1,2]
    dy=[1,2,2,1,-1,-2,-2,-1]

    T=int(input())

    for i in range(T):
        N = int(input())
        q = deque()
        graph = [[0]*N for _ in range(N)]
        start  = list(map(int,input().split()))
        goal = list(map(int,input().split()))
        q.append((start[0],start[1]))
        print(bfs(goal))