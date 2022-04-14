def bt(x):
    if len(check) == M:
        print(*check)
        return
    for i in range(x, N + 1):
        check.append(i)
        bt(i)
        check.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    check = []
    bt(1)
