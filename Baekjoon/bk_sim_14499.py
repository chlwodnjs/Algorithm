from collections import deque


def rotate(dir):
    if dir == 1:
        res[1], res[3], res[4], res[6] = res[3], res[6], res[1], res[4]
    elif dir == 2:
        res[1], res[3], res[4], res[6] = res[4], res[1], res[6], res[3]
    elif dir == 3:
        res[1], res[2], res[5], res[6] = res[2], res[6], res[1], res[5]
    elif dir == 4:
        res[1], res[2], res[5], res[6] = res[5], res[1], res[6], res[2]


def move(dir):
    if dir == 1:
        return 0, 1
    elif dir == 2:
        return 0, -1
    elif dir == 3:
        return -1, 0
    else:
        return 1, 0


def sim():
    global x, y
    while q:
        flag = q.popleft()
        a, b = move(flag)
        if 0 <= x + a < N and 0 <= y + b < M:
            x += a
            y += b
            rotate(flag)
            if graph[x][y] == 0:
                graph[x][y] = res[1]
            else:
                res[1] = graph[x][y]
                graph[x][y] = 0
            print(res[6])


if __name__ == '__main__':
    N, M, x, y, K = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    q = deque(map(int, input().split()))
    res = [0] * 7
    sim()
