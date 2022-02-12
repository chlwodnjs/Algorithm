def bt(x):
    if len(graph) == M:
        if sorted(graph)==graph:
            print(*graph)
            return
    for i in range(N):
        if check[i] not in graph:
            graph.append(check[i])
            bt(x + 1)
            graph.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    check = list(map(int, input().split()))
    check = sorted(check)
    graph = []
    bt(0)
