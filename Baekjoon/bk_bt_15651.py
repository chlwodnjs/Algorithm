def bt(x):
    if x == M:
        for i in range(M):
            print(graph[i], end=' ')
        print()
    else:
        for i in range(1, N + 1):
            graph[x] = i
            bt(x + 1)


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [0] * 8
    bt(0)
