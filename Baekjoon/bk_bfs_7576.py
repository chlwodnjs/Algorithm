from collections import deque


def bfs():
    check = -1

    while q:
        check += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[x][y]
                        q.append((nx, ny))
    for t in graph:
        if 0 in t:
            return -1
    return check


if __name__ == "__main__":
    M, N = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                q.append((i, j))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    print(bfs())
