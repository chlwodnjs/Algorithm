from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny]==1:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))
    return graph[N-1][M-1]


if __name__ == "__main__":

    N, M = map(int, input().split())
    graph = [list(map(int,input())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    print(bfs(0, 0))
