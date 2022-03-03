import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        x = q.popleft()
        for i in graph[x]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    count = 0

    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, N + 1):
        if not visited[i]:
            bfs(i)
            count += 1

    print(count)
