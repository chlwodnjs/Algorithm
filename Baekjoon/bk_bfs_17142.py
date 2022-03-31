from collections import deque
from itertools import combinations
import sys


def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if vis[nx][ny] == 0 and graph[nx][ny] != 1:
                    ans[nx][ny] = ans[x][y] + 1
                    vis[nx][ny] = 1
                    q.append((nx, ny))


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    check = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    check_res = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                check.append([i, j])
            if graph[i][j] != 1:
                check_res += 1
    comb = list(combinations(check, M))
    res = sys.maxsize

    for c in comb:
        q = deque()
        ans = [[-1] * N for _ in range(N)]
        vis = [[0] * N for _ in range(N)]
        for a, b in c:
            ans[a][b] = 0
            vis[a][b] = 1
            q.append((a, b))
        bfs()
        flag = 0
        for v in vis:
            flag += sum(v)

        if flag == check_res:
            xx = 0
            for i in range(N):
                for j in range(N):
                    if graph[i][j] != 1 and [i, j] not in check:
                        xx = max(xx, ans[i][j])
            res = min(res, xx)
    if res != sys.maxsize:
        print(res)
    else:
        print(-1)
