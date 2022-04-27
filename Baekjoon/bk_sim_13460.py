from collections import deque


def bfs():
    res = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()

            if res > 10:
                return -1
            if graph[rx][ry] == 'O':
                return res

            for k in range(4):
                nx, ny = rx, ry
                while 1:
                    nx += dx[k]
                    ny += dy[k]
                    if graph[nx][ny] == '#':
                        nx -= dx[k]
                        ny -= dy[k]
                        break
                    if graph[nx][ny] == 'O':
                        break
                mx, my = bx, by
                while 1:
                    mx += dx[k]
                    my += dy[k]
                    if graph[mx][my] == '#':
                        mx -= dx[k]
                        my -= dy[k]
                        break
                    if graph[mx][my] == 'O':
                        break
                if graph[mx][my] == 'O':
                    continue

                if mx == nx and my == ny:
                    if abs(nx - rx) + abs(ny - ry) > abs(mx - bx) + abs(my - by):
                        nx -= dx[k]
                        ny -= dy[k]
                    else:
                        mx -= dx[k]
                        my -= dy[k]
                if (nx, ny, mx, my) not in vis:
                    vis.append((nx, ny, mx, my))
                    q.append((nx, ny, mx, my))
        res += 1
    return -1


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(input()) for _ in range(N)]
    vis = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 'R':
                rqx, rqy = i, j
            if graph[i][j] == 'B':
                bqx, bqy = i, j
    q.append((rqx, rqy, bqx, bqy))
    vis.append((rqx, rqy, bqx, bqy))
    print(bfs())
