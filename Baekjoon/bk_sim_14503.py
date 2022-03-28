from collections import deque


def bfs():
    global res
    while q:
        x, y, check = q.popleft()
        graph[x][y] = 2
        nd = check
        for k in range(4):
            nd = (nd+3) % 4
            nx = x + dx[nd]
            ny = y + dy[nd]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 0:
                q.append((nx, ny, nd))
                graph[nx][ny] = 2
                res += 1
                break
            elif k == 3:
                nd = (check+2) % 4
                nx = x + dx[nd]
                ny = y + dy[nd]
                q.append((nx, ny, check))
                if graph[nx][ny] == 1:
                    return res
    return res


if __name__ == '__main__':
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    res = 1
    q.append((r, c, d))
    print(bfs())
