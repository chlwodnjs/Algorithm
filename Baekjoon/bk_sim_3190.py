from collections import deque


def check(c, s):
    if c == 'L':
        s = (s - 1) % 4
    else:
        s = (s + 1) % 4
    return s


if __name__ == '__main__':
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    res = 1
    snake_dir = 1
    dir = {}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    K = int(input())

    for _ in range(K):
        apple_x, apple_y = map(int, input().split())
        graph[apple_x - 1][apple_y - 1] = 1
    L = int(input())

    for _ in range(L):
        X, C = input().split()
        dir[int(X)] = C

    x, y = 0, 0
    graph[x][y] = 2
    q = deque()
    q.append((x, y))
    while 1:
        x += dx[snake_dir]
        y += dy[snake_dir]
        if 0 <= x < N and 0 <= y < N and not graph[x][y] == 2:
            if not graph[x][y] == 1:
                a, b = q.popleft()
                graph[a][b] = 0
            q.append((x, y))
            graph[x][y] = 2
            if res in dir.keys():
                snake_dir = check(dir[res], snake_dir)
            res += 1

        else:
            print(res)
            break
