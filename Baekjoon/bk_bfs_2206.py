from collections import deque


def bfs():
    check_list[0][0][1] = 1
    while q:
        x, y, z = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < M:
                if nx == N - 1 and ny == M - 1:
                    return check_list[x][y][z] + 1
                elif graph[nx][ny] == 1 and z == 1:
                    q.append((nx, ny, 0))
                    check_list[nx][ny][0] = check_list[x][y][1] + 1
                elif graph[nx][ny] == 0 and check_list[nx][ny][z] == 0:
                    q.append((nx, ny, z))
                    check_list[nx][ny][z] = check_list[x][y][z] + 1
    return -1


if __name__ == '__main__':
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    N, M = map(int, input().split())

    graph = [list(map(int, input())) for _ in range(N)]
    check_list = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    q.append((0, 0, 1))
    print(bfs())
