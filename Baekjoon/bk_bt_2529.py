def sort_func(i, j, k):
    if k == ">":
        return i > j
    else:
        return i < j


def bt(x, s):
    if x > k:
        res.append(s)
        return
    for i in range(10):
        if not visit[i]:
            if not x or sort_func(s[-1], str(i), check[x - 1]):
                visit[i] = 1
                bt(x + 1, s + str(i))
                visit[i] = 0


if __name__ == '__main__':
    k = int(input())
    check = list(map(str, input().split()))
    visit = [0] * 10
    res = []
    bt(0, "")
    print(res[-1])
    print(res[0])
