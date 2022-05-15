from collections import deque


def bfs(cnt, x):
    q = deque()
    q.append((0, x))
    vis = [0] * N
    res = 0
    vis[x] = 1

    while q:
        check1, check2 = q.popleft()
        for arr in graph[check2]:
            if not vis[arr[1]] and arr[0] >= cnt:
                vis[arr[1]] = 1
                q.append(arr)
                res += 1
    return res


if __name__ == '__main__':
    N, Q = map(int, input().split())
    graph = [[] for _ in range(N)]

    for _ in range(N - 1):
        p, q, r = map(int, input().split())
        graph[p - 1].append((r, q - 1))
        graph[q - 1].append((r, p - 1))

    for _ in range(Q):
        k, v = map(int, input().split())
        print(bfs(k, v-1))
