def zfunc(n, r, c):
    if n == 0:
        return 0
    flag = 2 ** (n - 1)
    if r < flag and c < flag:
        return zfunc(n - 1, r, c)
    if r < flag and c >= flag:
        return flag * flag + zfunc(n - 1, r, c-flag)
    if r >= flag and c < flag:
        return 2 * flag * flag + zfunc(n - 1, r-flag, c)
    return 3 * flag * flag + zfunc(n - 1, r-flag, c-flag)


if __name__ == '__main__':
    N, R, C = map(int, input().split())
    print(zfunc(N, R, C))
