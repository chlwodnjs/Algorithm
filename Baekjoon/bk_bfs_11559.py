from collections import deque


def bfs(i, j):
    q.append((i, j))
    check_graph.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if vis[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                    q.append((nx, ny))
                    check_graph.append((nx, ny))
                    vis[nx][ny] = 1


def sim():
    for i in range(M):
        for j in reversed(range(N - 1)):
            for k in range(N - 1, j, -1):
                if graph[j][i] != '.' and graph[k][i] == '.':
                    graph[k][i] = graph[j][i]
                    graph[j][i] = '.'
                    break


if __name__ == '__main__':
    N, M = 12, 6
    graph = [list(input()) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    res = 0

    while 1:
        vis = [[0] * M for _ in range(N)]
        check = 0

        for i in range(N):
            for j in range(M):
                if graph[i][j] != '.' and vis[i][j] == 0:
                    check_graph = []
                    q = deque()
                    vis[i][j] = 1
                    bfs(i, j)
                    if len(check_graph) >= 4:
                        check = 1
                        for x, y in check_graph:
                            graph[x][y] = '.'
        if check == 0:
            break
        sim()
        res += 1
    print(res)
