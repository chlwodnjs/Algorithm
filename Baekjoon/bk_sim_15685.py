def sim(res):
    for i in range(100):
        for j in range(100):
            if graph[i][j] == 1 and graph[i + 1][j] == 1 and graph[i][j + 1] == 1 and graph[i + 1][j + 1] == 1:
                res += 1
    return res


if __name__ == '__main__':
    N = int(input())
    graph = [[0] * 101 for _ in range(101)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    for i in range(N):
        x, y, d, g = map(int, input().split())
        graph[y][x] = 1
        check = [d]

        for j in range(g):
            for k in reversed(range(len(check))):
                check.append((check[k] + 1) % 4)

        for m in range(len(check)):
            nx = x + dx[check[m]]
            ny = y + dy[check[m]]
            if 0 <= nx < 101 and 0 <= ny < 101:
                graph[ny][nx] = 1
            x = nx
            y = ny

    print(sim(0))
