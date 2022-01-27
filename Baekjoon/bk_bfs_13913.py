from collections import deque


def bfs():
    while q:
        x = q.popleft()
        if x == K:
            return graph[x]

        for k in (x - 1, x + 1, 2 * x):
            if 0 <= k < m and graph[k] == 0:
                graph[k] = graph[x] + 1
                check[k] = x
                q.append(k)


def path(K, N):
    result = []
    while K != N:
        result.append(K)
        K = check[K]
    result.append(N)
    result.reverse()
    print(*result)


if __name__ == '__main__':
    q = deque()
    m = 100001
    N, K = map(int, input().split())
    graph = [0] * m
    check = [0] * m
    q.append(N)
    print(bfs())
    path(K, N)
