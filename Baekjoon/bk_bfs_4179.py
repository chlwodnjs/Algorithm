from collections import deque


def bfs():
    bul = 'IMPOSSIBLE'
    while dq:
        x1, y1 = dq.popleft()

        for k1 in range(4):
            mx = x1 + dx[k1]
            my = y1 + dy[k1]

            if 0 <= mx < R and 0 <= my < C:
                if not fire[mx][my] and graph[mx][my] == '.' or graph[mx][my] == 'J':
                    fire[mx][my] = fire[x1][y1] + 1
                    dq.append((mx, my))
    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < R and 0 <= ny < C:
                if not ji[nx][ny] and graph[nx][ny] == '.' :
                    if not fire[nx][ny] or fire[nx][ny] > ji[x][y] + 1:
                        ji[nx][ny] = ji[x][y] + 1
                        q.append((nx, ny))
            else:
                return ji[x][y]+1

    return bul


if __name__ == "__main__":
    R, C = map(int, input().split())
    graph = [list(map(str, input())) for _ in range(R)]
    ji = [[0] * C for _ in range(R)]
    fire = [[0] * C for _ in range(R)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    dq = deque()
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 'J':
                q.append((i, j))
            elif graph[i][j] == 'F':
                dq.append((i, j))

    print(bfs())
