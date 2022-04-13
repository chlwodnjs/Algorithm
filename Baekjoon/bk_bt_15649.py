def bt(x):
    if x == M:
        for i in range(M):
            print(' '.join(map(str,check)))
            return
    for i in range(1, N + 1):
        if not vis[i]:
            check.append(i)
            vis[i] = 1
            bt(x + 1)
            check.pop()
            vis[i] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    check, vis = [], [0] * 9
    bt(0)
