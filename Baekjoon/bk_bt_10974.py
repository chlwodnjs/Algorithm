def bt(x):
    if len(check) == N:
        print(*check)
        return
    for i in range(1,N+1):
        if i not in check:
            check.append(i)
            bt(x+1)
            check.pop()


if __name__ == '__main__':
    N = int(input())
    check= []
    bt(1)
