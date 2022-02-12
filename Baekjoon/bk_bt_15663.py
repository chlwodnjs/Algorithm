def bt(x):
    if x == M:
        print(*graph)
        return
    flag = 0
    for i in range(N):
        if not visit[i] and not flag == check[i]:
            graph.append(check[i])
            visit[i] = 1
            flag = check[i]
            bt(x + 1)
            visit[i] = 0
            graph.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    check = list(map(int, input().split()))
    check = sorted(check)
    graph = []
    visit = [0] * N
    bt(0)