from collections import deque


def bfs():
    while q:
        x, y, z, cnt = q.popleft()
        if x == N - 1 and y == M - 1:
            return cnt
        for dx,dy in dr:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] == 1 and z < K and not check[nx][ny][z+1]:
                    q.append([nx, ny, z + 1, cnt + 1])
                    check[nx][ny][z + 1] = 1
                elif graph[nx][ny] == 0 and not check[nx][ny][z]:
                    q.append([nx, ny, z, cnt + 1])
                    check[nx][ny][z] = 1
    return -1


if __name__ == '__main__':
    q = deque()
    # dx = [1, 0, -1, 0]
    # dy = [0, 1, 0, -1]
    dr = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    N, M, K = map(int, input().split())
    check = [[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
    graph = [list(map(int, input())) for _ in range(N)]
    q.append([0, 0, 0, 1])
    check[0][0][0] = 1
    print(bfs())
