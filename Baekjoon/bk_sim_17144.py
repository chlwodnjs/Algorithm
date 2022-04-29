def bfs():
    sp = [[0] * C for _ in range(R)]

    for x in range(R):
        for y in range(C):
            cnt = 0
            if graph[x][y] and graph[x][y] != -1:
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < R and 0 <= ny < C:
                        if graph[nx][ny] != -1:
                            sp[nx][ny] += graph[x][y] // 5
                            cnt += 1
                graph[x][y] -= (graph[x][y] // 5) * cnt

    for i in range(R):
        for j in range(C):
            graph[i][j] += sp[i][j]


def sim():
    flag = 0
    k = 0

    x, y = clean[0], 1
    while 1:
        nx = x + udx[k]
        ny = y + udy[k]
        if x == clean[0] and y == 0:
            break
        if 0 > nx or R <= nx or 0 > ny or C <= ny:
            k += 1
            continue
        graph[x][y], flag = flag, graph[x][y]
        x, y = nx, ny

    flag = 0
    k = 0

    x, y = clean[1], 1

    while 1:
        nx = x + ddx[k]
        ny = y + ddy[k]
        if x == clean[1] and y == 0:
            break
        if 0 > nx or R <= nx or 0 > ny or C <= ny:
            k += 1
            continue
        graph[x][y], flag = flag, graph[x][y]
        x, y = nx, ny


if __name__ == '__main__':
    R, C, T = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(R)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    udx = [0, -1, 0, 1]
    udy = [1, 0, -1, 0]
    ddx = [0, 1, 0, -1]
    ddy = [1, 0, -1, 0]
    clean = []

    for i in range(R):
        for j in range(C):
            if graph[i][j] == -1:
                clean.append(i)

    for _ in range(T):
        bfs()
        sim()

    res = 0
    for i in range(R):
        for j in range(C):
            if graph[i][j] != -1:
                res += graph[i][j]
    print(res)
