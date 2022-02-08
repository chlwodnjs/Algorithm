from collections import deque


def bfs():
    global check
    cnt = 1
    while q:
        flag = 0
        for _ in range(len(q)):
            x, y = q.popleft()

            if check[x][y] == 0:
                q.append((x, y))
                continue

            flag = 1
            if graph[x][y] != 0:
                for x1, y1 in light[graph[x][y]]:
                    if check[x1][y1] == 0:
                        check[x1][y1] = 1
                        cnt += 1

            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 < nx < N+1 and 0 < ny < N+1 and visit[nx][ny] != 1:
                    if check[nx][ny] != -1:
                        visit[nx][ny] = 1
                        q.append((nx, ny))
        if not flag:
            break
    return cnt


if __name__ == '__main__':
    q = deque([(1, 1)])
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    N, M = map(int, input().split())

    graph = [[0] * (N + 1) for _ in range(N + 1)]
    visit = [[0] * (N + 1) for _ in range(N + 1)]
    check = [[-1] * (N + 1) for _ in range(N + 1)]

    light = [[]]

    for i in range(M):
        x, y, x1, y1 = (map(int, input().split()))
        if graph[x][y] == 0:
            graph[x][y] = len(light)
            light.append([(x1, y1)])
        else:
            light[graph[x][y]].append((x1, y1))
        check[x1][y1] = 0

    visit[1][1] = 1
    check[1][1] = 1
    print(bfs())
