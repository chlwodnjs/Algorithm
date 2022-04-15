def bt(x):
    if len(check) == M:
        print(*check)
        return
    for i in range(x, N):
        check.append(arr[i])
        bt(i)
        check.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    check = []
    bt(0)
