from collections import deque


def bfs():
    while q:
        x, y, z = q.popleft()
        if x == H - 1 and y == W - 1:
            return visit[x][y][z]
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < H and 0 <= ny < W:
                if graph[nx][ny] == 0 and visit[nx][ny][z] == 0:
                    visit[nx][ny][z] = visit[x][y][z] + 1
                    q.append((nx, ny, z))
        if z > 0:
            for k in range(8):
                nx = x + bx[k]
                ny = y + by[k]
                if 0 <= nx < H and 0 <= ny < W:
                    if graph[nx][ny] == 0 and visit[nx][ny][z - 1] == 0:
                        visit[nx][ny][z - 1] = visit[x][y][z] + 1
                        q.append((nx, ny, z - 1))
    return -1


if __name__ == '__main__':
    K = int(input())
    W, H = map(int, input().split())

    graph = [list(map(int, input().split())) for _ in range(H)]
    visit = [[[0 for _ in range(K+1)] for _ in range(W)] for _ in range(H)]
    q = deque()
    bx = [2, 1, -1, -2, -2, -1, 1, 2]
    by = [1, 2, 2, 1, -1, -2, -2, -1]
    dx = [1, 0, -1, 0, 1, 0, -1, 0]
    dy = [0, 1, 0, -1, 0, 1, 0, -1]

    q.append((0, 0, K))
    print(bfs())
