from collections import deque


def bfs(i, j):
    q = deque()
    q.append((i, j))
    temp = [[i, j]]
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not vis[nx][ny]:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    q.append((nx, ny))
                    temp.append([nx, ny])
                    vis[nx][ny] = 1
    return temp


if __name__ == '__main__':
    N, L, R = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = 0
    while 1:
        vis = [[0] * N for _ in range(N)]
        flag = 1
        for i in range(N):
            for j in range(N):
                if not vis[i][j]:
                    vis[i][j] = 1
                    check = bfs(i, j)
                    if len(check) > 1:
                        flag = 0
                        value = sum([graph[x][y] for x, y in check]) // len(check)
                        for x, y in check:
                            graph[x][y] = value
        if flag:
            break
        res += 1
    print(res)
