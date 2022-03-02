from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        if y + 1 not in check_bfs:
            check_bfs.append(y + 1)
        if len(check_bfs) == N:
            return
        for i in range(N):
            if graph[y][i] == 1:
                graph[y][i] = 0
                q.append((y, i))
    return


def dfs(x):
    if len(check_dfs) == N:
        return
    for i in range(N):
        if graph[x][i] == 1 and not visit[x][i]:
            visit[x][i] = 1
            if i+1 not in check_dfs:
                check_dfs.append(i + 1)
                dfs(i)


if __name__ == '__main__':
    N, M, V = map(int, input().split())
    graph = [[0] * N for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    for _ in range(M):
        i, j = map(int, input().split())
        graph[i - 1][j - 1] = 1
        graph[j - 1][i - 1] = 1
    q = deque()
    check_bfs = [V]
    check_dfs = [V]
    for i in range(N):
        if graph[V - 1][i] == 1:
            q.append((V - 1, i))
    dfs(V - 1)
    bfs()
    print(*check_dfs)
    print(*check_bfs)
