import sys

input = sys.stdin.readline


def dfs(x, y, check, flag):
    global res, Mmax

    vis[x][y] = 1
    if check == 3:
        res = max(res, flag)
        return
    if flag + (3 - check) * Mmax <= res:
        return

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M and not vis[nx][ny]:
            dfs(nx, ny, check + 1, flag + graph[nx][ny])
            vis[nx][ny] = 0


def mmod(x, y, graph):
    global res
    checkarr = []
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            checkarr.append(graph[nx][ny])
    if len(checkarr) > 2:
        flag = graph[x][y] + sum(sorted(checkarr, reverse=True)[:3])
        res = max(res, flag)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    vis = [[0] * M for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = 0
    Mmax = max(map(max, graph))

    for i in range(N):
        for j in range(M):
            dfs(i, j, 0, graph[i][j])
            vis[i][j] = 0
            mmod(i, j, graph)
    print(res)