from collections import deque


def bfs():
    while q:
        x = q.popleft()
        if x == K:
            return graph[x]
        else:
            for i in (x - 1, x + 1, x * 2):
                if 0 <= i < M and not graph[i]:
                    if i == 2 * x and x > 0:
                        graph[i] = graph[x]
                        q.appendleft(i)
                    else:
                        graph[i] = graph[x] + 1
                        q.append(i)


if __name__ == "__main__":
    M = 100001
    N, K = map(int, input().split())
    graph = [0] * M
    q = deque()
    q.append(N)

    print(bfs())
