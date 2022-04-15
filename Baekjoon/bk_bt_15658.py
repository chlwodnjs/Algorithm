def bt(x):
    if len(check) == M:
        print(*check)
        return
    flag = 0
    for i in range(N):
        if not vis[i] and not flag == arr[i]:
            check.append(arr[i])
            flag = arr[i]
            vis[i] = 1
            bt(x + 1)
            vis[i] = 0
            check.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    check = []
    vis = [0]*9
    bt(0)
