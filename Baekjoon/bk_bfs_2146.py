import sys
from collections import deque


def bfs(tmp):
    while q:
        x, y = q.popleft()
        graph[x][y] = check
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 1 and visit[nx][ny] == 0:
                    q.append((nx, ny))
                    visit[nx][ny] = 1
                    graph[nx][ny] = tmp


def dist_bfs(tmp, result):
    dist = [[-1] * N for _ in range(N)]
    q1 = deque()

    for i in range(N):
        for j in range(N):
            if graph[i][j] == tmp:
                q1.append((i, j))
                dist[i][j] = 0
    while q1:
        x1, y1 = q1.popleft()
        for k1 in range(4):
            nx1 = x1 + dx[k1]
            ny1 = y1 + dy[k1]
            if 0 <= nx1 < N and 0 <= ny1 < N:
                if graph[nx1][ny1] > 0 and graph[nx1][ny1] != tmp:
                    return check_list.append(min(result, dist[x1][y1]))

                if graph[nx1][ny1] == 0 and dist[nx1][ny1] == -1:
                    q1.append((nx1, ny1))
                    dist[nx1][ny1] = dist[x1][y1] + 1


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * N for _ in range(N)]
    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    check = 1
    check_list = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 and visit[i][j] == 0:
                q.append((i, j))
                visit[i][j] = 1
                bfs(check)
                check += 1

    res = sys.maxsize

    for c in range(1, check):
        dist_bfs(c, res)
    print(min(check_list))
