def bt(i, j):
    global H
    if i == N - 1 and j == M - 1:
        return 1
    if vis[i][j] != -1:
        return vis[i][j]
    vis[i][j] = 0
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] < graph[i][j]:
                vis[i][j] += bt(nx, ny)

    return vis[i][j]


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    vis = [[-1] * M for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    H = bt(0, 0)
    print(H)
