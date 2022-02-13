def bt(x):
    if len(graph) == 6:
        print(*graph)
        return
    for i in range(x, K):
        if not visit[i]:
            graph.append(check[i])
            visit[i] = 1
            bt(i)
            graph.pop()
            visit[i] = 0


if __name__ == '__main__':
    while 1:
        check = list(map(int, input().split()))
        if check[0] == 0:
            break
        K = check.pop(0)
        graph = []
        visit = [0] * K
        bt(0)
        print()
