def bt(x, a, c1, c2, c3, c4):
    if x == N:
        res.append(a)
        return

    if c1:
        bt(x + 1, a + check[x], c1-1, c2, c3, c4)
    if c2:
        bt(x + 1, a - check[x], c1, c2-1, c3, c4)
    if c3:
        bt(x + 1, a * check[x], c1, c2, c3-1, c4)
    if c4:
        bt(x + 1, int(a / check[x]), c1, c2, c3, c4-1)


if __name__ == '__main__':
    N = int(input())
    check = list(map(int, input().split()))
    cal = list(map(int, input().split()))
    res = []
    bt(1, check[0], cal[0], cal[1], cal[2], cal[3])
    res = sorted(res)
    print(res[-1])
    print(res[0])
