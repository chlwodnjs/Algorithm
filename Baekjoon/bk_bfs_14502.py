from collections import deque


def bfs():
    global result
    flag = 0
    q = deque()
    copy_graph = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            copy_graph[i][j] = graph[i][j]

    for i in range(N):
        for j in range(M):
            if copy_graph[i][j] == 2:
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                q.append((nx, ny))

    for i in copy_graph:
        for j in i:
            if j == 0:
                flag += 1
    result = max(result, flag)


def check(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                check(cnt + 1)
                graph[i][j] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    result = 0
    check(0)
    print(result)
