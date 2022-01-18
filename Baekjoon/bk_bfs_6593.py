from collections import deque


def bfs():
    while q:
        z, y, x = q.popleft()
        for k in range(6):
            nx = x + dx[k]
            ny = y + dy[k]
            nz = z + dz[k]

            if 0 <= nx < C and 0 <= ny < R and 0 <= nz < L:
                if end[nz][ny][nx] == 0:
                    if graph[nz][ny][nx] == '.':
                        q.append((nz, ny, nx))
                        end[nz][ny][nx] = end[z][y][x] + 1
                    elif graph[nz][ny][nx] == 'E':
                        return print('Escaped in', end[z][y][x], 'minute(s).')
    return print('Trapped!')


if __name__ == '__main__':

    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]

    while 1:
        q = deque()
        L, R, C = map(int, input().split())
        if L == 0 and R == 0 and C == 0:
            break
        graph = []
        end = []
        for i in range(L):
            ap = [list(map(str, input())) for _ in range(R)]
            graph.append(ap)
            e_ = [[0] * C for _ in range(R)]
            end.append(e_)
            input()

        for l in range(L):
            for r in range(R):
                for c in range(C):
                    if graph[l][r][c] == 'S':
                        q.append((l, r, c))
                        end[l][r][c] = 1
                        bfs()
