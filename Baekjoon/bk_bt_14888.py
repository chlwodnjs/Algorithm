def bt(x, val, a, b, c, d):
    if x == N - 1:
        res.append(val)
        return

    if a:
        bt(x + 1, val + num[x + 1], a - 1, b, c, d)
    if b:
        bt(x + 1, val - num[x + 1], a, b - 1, c, d)
    if c:
        bt(x + 1, val * num[x + 1], a, b, c - 1, d)
    if d:
        bt(x + 1, int(val / num[x + 1]), a, b, c, d - 1)


if __name__ == '__main__':
    N = int(input())
    num = list(map(int, input().split()))
    a, b, c, d = map(int, input().split())
    res = []
    bt(0, num[0], a, b, c, d)
    print(max(res), min(res))
