def bt(m):
    if m == M:
        if sorted(graph) == graph:
            print(*graph)
        return
    for i in range(1, N + 1):
        if not check[i]:
            graph.append(i)
            check[i] = 1
            bt(m + 1)
            graph.pop()
            check[i] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = []
    check = [0] * 9
    bt(0)
