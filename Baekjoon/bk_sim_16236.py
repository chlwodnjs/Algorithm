from collections import deque
import sys


def bfs(sx, sy):
    global weight, check, res

    while 1:
        q = deque()
        q.append((sx, sy, 0))
        vis = [[0] * N for _ in range(N)]
        flag = sys.maxsize
        fish = []
        while q:
            x, y, count = q.popleft()

            if count > flag:
                break
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]

                if 0 <= nx < N and 0 <= ny < N and not vis[nx][ny]:
                    if graph[nx][ny] > weight:
                        continue
                    if graph[nx][ny] != 0 and graph[nx][ny] < weight:
                        fish.append((nx, ny, count + 1))
                        flag = count
                    vis[nx][ny] = 1
                    q.append((nx, ny, count + 1))

        if len(fish) > 0:
            fish.sort()
            x, y, dist = fish[0][0], fish[0][1], fish[0][2]
            res += dist
            check += 1
            graph[x][y] = 0
            if check == weight:
                weight += 1
                check = 0
            sx, sy = x, y
        else:
            break


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    weight = 2
    check = 0
    res = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                graph[i][j] = 0
                bfs(i, j)
    print(res)
