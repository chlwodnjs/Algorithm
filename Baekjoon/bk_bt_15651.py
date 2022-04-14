def bt(x):
    if x == M:
        print(*check)
        return
    for i in range(1, N + 1):
        check.append(i)
        bt(x + 1)
        check.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    check = []
    bt(0)
