from copy import deepcopy
import sys


def fill(x, y, tmp, d):
    for k in d:
        nx = x + dx[k]
        ny = y + dy[k]
        while 0 <= nx < N and 0 <= ny < M:
            if tmp[nx][ny] == 6:
                break
            elif tmp[nx][ny] == 0:
                tmp[nx][ny] = "#"
            nx += dx[k]
            ny += dy[k]


def bt(flag, graph):
    global res
    temp = deepcopy(graph)
    if flag == cctv_cnt:
        num = 0
        for i in range(N):
            for j in range(M):
                if temp[i][j] == 0:
                    num += 1
        res = min(res, num)
        return
    cctv, x, y = check[flag]
    for dir in direction[cctv]:
        fill(x, y, temp, dir)
        bt(flag+1, temp)
        temp = deepcopy(graph)


if __name__ == '__main__':
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[3, 0], [0, 2], [2, 1], [1, 3]],
                 [[1, 3, 0], [3, 0, 2], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    check = []
    cctv_cnt = 0
    res = sys.maxsize

    for i in range(N):
        for j in range(M):
            if graph[i][j] in [1, 2, 3, 4, 5]:
                check.append([graph[i][j], i, j])
                cctv_cnt += 1
    bt(0, graph)
    print(res)
