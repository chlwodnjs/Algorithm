def bt(x):
    if x == M:
        print(*graph)
        return
    flag = 0
    for i in range(N):
        if flag != check[i]:
            graph.append(check[i])
            flag = check[i]
            bt(x + 1)
            graph.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    check = list(map(int, input().split()))
    check = sorted(check)
    graph = []
    bt(0)
