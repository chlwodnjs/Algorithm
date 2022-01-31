from collections import deque


def bfs1(check, p, num):
    global flag
    res = []
    q = deque(check)

    for i in range(num):
        if not flag or len(q) == 0:
            return res
        for _ in range(len(q)):
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == '.':
                    graph[nx][ny] = p + 1
                    result[p] += 1
                    flag -= 1
                    q.append((nx, ny))
                    if i == num - 1:
                        res.append((nx, ny))
    return res


def bfs2(x, y):
    global flag
    q = deque([(x, y)])
    visit[x][y] = 1
    while q:
        x, y = q.popleft()
        flag += 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny] and graph[nx][ny] == '.':
                visit[nx][ny] = 1
                q.append((nx, ny))
    flag -= 1


if __name__ == '__main__':
    N, M, P = map(int, input().split())
    p_list = list(map(int, input().split()))
    graph = [list(input()) for _ in range(N)]
    result = [0] * P
    check = [[] for _ in range(P)]
    flag = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit = [[0]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] != '.' and graph[i][j] != '#':
                graph[i][j] = int(graph[i][j])
                bfs2(i, j)
                result[graph[i][j] - 1] += 1
                check[graph[i][j] - 1].append((i, j))
    while flag:
        for i in range(P):
            check[i] = bfs1(check[i], i, p_list[i])

    print(*result)
