def bt(x):
    vis[x] = 1
    for i in range(L):
        if check[x][i] and not vis[i]:
            bt(i)


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = N + 2
        graph = [list(map(int, input().split())) for _ in range(L)]
        check = [[0] * L for _ in range(L)]
        vis = [0] * L
        for i in range(L):
            for j in range(L):
                if abs(graph[i][0] - graph[j][0]) + abs(graph[i][1] - graph[j][1]) <= 1000:
                    check[i][j] = 1
                    check[j][i] = 1

        bt(0)
        print("happy" if vis[L - 1] == 1 else "sad")
