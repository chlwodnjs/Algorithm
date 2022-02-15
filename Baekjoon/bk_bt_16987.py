def bt(x):
    global res

    if x == N:
        check = 0
        for i in Stat:
            if i <= 0:
                check += 1
        if check > res:
            res = check
        return

    if Stat[x] > 0:
        for i in range(N):
            flag = 0
            if Stat[i] > 0 and i != x:
                flag = 1
                Stat[i] -= Weight[x]
                Stat[x] -= Weight[i]
                bt(x + 1)
                Stat[i] += Weight[x]
                Stat[x] += Weight[i]
        if not flag:
            bt(x + 1)
    else:
        bt(x + 1)


if __name__ == '__main__':
    N = int(input())
    Stat = [0] * N
    Weight = [0] * N

    for _ in range(N):
        Stat[_], Weight[_] = map(int, input().split())

    res = 0
    bt(0)
    print(res)
