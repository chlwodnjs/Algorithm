def bt(x):
    if len(graph) == M:
        print(*graph)
        return
    for i in range(N):
        graph.append(check[i])
        bt(x + 1)
        graph.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    check = list(map(int, input().split()))
    check = sorted(check)
    graph = []
    bt(0)
