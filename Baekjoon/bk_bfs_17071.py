from collections import deque


def bfs(q, K):
    cnt = 0
    flag = 0
    while q:
        if K >= m:
            return -1
        if graph[flag][K]:
            return cnt
        dq = deque()
        flag = flag ^ 1

        for x in q:
            for i in (x - 1, x + 1, x * 2):
                if 0 <= i < m and not graph[flag][i]:
                    graph[flag][i] = 1
                    dq.append(i)
        cnt += 1
        K += cnt
        q = dq


if __name__ == '__main__':
    N, K = map(int, input().split())
    m = 500001
    graph = [[0] * m for _ in range(2)]
    graph[0][N] = 1
    q = deque()
    q.append(N)
    print(bfs(q, K))
