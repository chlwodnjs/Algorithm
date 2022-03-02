from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        if y not in check:
            check.append(y)
        for i in range(N):
            if graph[y][i] == 1:
                graph[y][i] = 0
                q.append((y, i))
    return


if __name__ == '__main__':
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    q = deque()
    check = [0]
    for i in range(int(input())):
        x, y = map(int, input().split())
        graph[x - 1][y - 1] = 1
        graph[y - 1][x - 1] = 1
        if x == 1:
            q.append((x - 1, y - 1))
    bfs()
    print(len(check) - 1)
