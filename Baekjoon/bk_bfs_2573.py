from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        visit[x][y] = 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 0:
                    check_count[x][y] += 1
                elif graph[nx][ny] != 0 and visit[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx, ny))


if __name__ == '__main__':
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    res = 0
    flag = 0
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    while 1:
        visit = [[0] * M for _ in range(N)]
        check_count = [[0] * M for _ in range(N)]
        check = 0

        for i in range(N):
            for j in range(M):
                if graph[i][j] != 0 and visit[i][j] == 0:
                    q.append((i, j))
                    bfs()
                    check += 1

        for i in range(N):
            for j in range(M):
                graph[i][j] -= check_count[i][j]
                if graph[i][j] < 0:
                    graph[i][j] = 0

        if check == 0:
            break
        elif check >= 2:
            flag = 1
            break
        res += 1
    if flag == 1:
        print(res)
    else:
        print(0)
