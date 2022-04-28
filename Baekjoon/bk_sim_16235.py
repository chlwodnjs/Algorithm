from collections import deque


def ss():
    for i in range(N):
        for j in range(N):
            for k in range(len(q[i][j])):
                if graph[i][j] < q[i][j][k]:
                    for _ in range(k, len(q[i][j])):
                        dT[i][j].append(q[i][j].pop())
                    break
                else:
                    graph[i][j] -= q[i][j][k]
                    q[i][j][k] += 1
    for i in range(N):
        for j in range(N):
            while dT[i][j]:
                graph[i][j] += (dT[i][j].pop()) // 2


def fw():
    for i in range(N):
        for j in range(N):
            for k in range(len(q[i][j])):
                if q[i][j][k] % 5 == 0:
                    for m in range(8):
                        nx = i + dx[m]
                        ny = j + dy[m]

                        if 0 <= nx < N and 0 <= ny < N:
                            q[nx][ny].appendleft(1)
            graph[i][j] += A[i][j]


if __name__ == '__main__':
    N, M, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    graph = [[5] * N for _ in range(N)]

    dT = [[[] for _ in range(N)] for _ in range(N)]

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    q = [[deque() for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        x, y, age = map(int, input().split())
        q[x-1][y-1].append(age)

    for _ in range(K):
        ss()
        fw()

    res = 0

    for i in range(N):
        for j in range(N):
            res += len(q[i][j])
    print(res)
