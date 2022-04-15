def bt(x):
    if len(check) == M:
        print(*check)
        return
    flag = 0
    for i in range(N):
        if not flag == arr[i]:
            check.append(arr[i])
            flag = arr[i]
            bt(x+1)
            check.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = sorted(arr)
    check = []
    bt(0)
