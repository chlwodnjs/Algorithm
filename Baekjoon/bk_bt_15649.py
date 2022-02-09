def bt(m):
    if m == M:
        for i in range(M):
            print(graph[i], end=' ')
        print()
        return
    for i in range(1, N + 1):
        if not check[i]:
            graph[m] = i
            check[i] = 1
            bt(m+1)
            check[i] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [0] * 9
    check = [0] * 9
    bt(0)
