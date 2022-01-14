from collections import deque


def bfs():
    check = 1
    while q:
        x, y = q.popleft()

        for p in range(4):
            nx = x + dx[p]
            ny = y + dy[p]

            if 0 <= nx < M and 0 <= ny < N:
                if graph[nx][ny] == 0:
                    q.append((nx, ny))
                    graph[nx][ny] = 1
                    check += 1
    return check_list.append(check)


if __name__ == '__main__':

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    M, N, K = map(int, input().split())
    q = deque()
    graph = [[0] * N for _ in range(M)]
    check_list = []
    for k in range(K):
        a, b, c, d = map(int, input().split())

        for i in range(b, d):
            for j in range(a, c):
                graph[i][j] = 1

    for n in range(N):
        for m in range(M):
            if graph[m][n] == 0:
                q.append((m, n))
                graph[m][n] = 1
                bfs()
    print(len(check_list))
    print(*sorted(check_list))
