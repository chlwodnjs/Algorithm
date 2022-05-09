def bt(x):
    for i in graph[x]:
        if not vis[i]:
            check[i] = check[x] + 1
            vis[i] = 1
            bt(i)
            vis[i] = 0


if __name__ == '__main__':
    N = int(input())
    A, B = map(int, input().split())
    M = int(input())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        x, y = map(int, input().split())
        graph[x - 1].append(y - 1)
        graph[y - 1].append(x-1)
    vis = [0] * N
    check = [0] * N

    bt(A-1)
    print(check[B-1] if check[B-1] > 0 else -1)
