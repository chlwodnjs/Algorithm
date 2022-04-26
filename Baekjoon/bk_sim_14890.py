def sim(check):
    vis = [0 for _ in range(N)]
    for i in range(1, N):
        if check[i - 1] == check[i]:
            continue

        if abs(check[i - 1] - check[i]) > 1:
            return 0

        if check[i - 1] > check[i]:
            for j in range(L):
                if i + j >= N or vis[i + j] or check[i] != check[i + j]:
                    return 0
                if check[i] == check[i + j]:
                    vis[i + j] = 1
        elif check[i - 1] < check[i]:
            for j in range(L):
                if i - j - 1 < 0 or vis[i - j - 1] or check[i - 1] != check[i - j - 1]:
                    return 0
                if check[i - 1] == check[i - j - 1]:
                    vis[i - j - 1] = 1

    return 1


if __name__ == '__main__':
    N, L = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    res = 0

    for i in range(N):

        res += sim(graph[i])
        res += sim([graph[j][i] for j in range(N)])

    print(res)
