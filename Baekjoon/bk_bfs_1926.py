from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    graph[x][y] = 0
    size = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny]:
                    q.append((nx, ny))
                    size += 1
                    graph[nx][ny] = 0
    return size


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    cnt = 0
    size_check = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j]:
                size_check = max(size_check, bfs(i, j))
                cnt += 1
    print(cnt)
    print(size_check)