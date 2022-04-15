def bt(x):
    if x == M and sorted(check) == check:
        print(*check)
        return
    for i in range(N):
        if arr[i] not in check:
            check.append(arr[i])
            bt(x + 1)
            check.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    check = []
    bt(0)
