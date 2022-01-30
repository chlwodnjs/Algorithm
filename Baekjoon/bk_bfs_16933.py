from collections import deque


def bfs():
    flag = True
    while q:
        x, y, z, res = q.popleft()
        if x == N - 1 and y == M - 1:
            return res
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and z != 0 and not check[nx][ny][z - 1]:
                    if flag:
                        check[nx][ny][z - 1] = 1
                        q.append((nx, ny, z - 1, res + 1))
                    else:
                        q.append((x, y, z, res + 1))
                if graph[nx][ny] == 0 and not check[nx][ny][z]:
                    check[nx][ny][z] = 1
                    q.append((nx, ny, z, res + 1))
        flag = not flag
    return -1


if __name__ == '__main__':
    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    N, M, K = map(int, input().split())
    check = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    graph = [list(map(int, input())) for _ in range(N)]
    q.append((0, 0, K, 1))
    check[0][0][K] = 1
    print(bfs())
