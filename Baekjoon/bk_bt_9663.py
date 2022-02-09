
def bt(n):
    global cnt
    if n == N:
        cnt += 1
        return
    for i in range(N):
        if not check1[i] and not check2[i + n] and not check3[n - i + N - 1]:
            check1[i] = 1
            check2[i + n] = 1
            check3[n - i + N - 1] = 1
            bt(n + 1)
            check1[i] = 0
            check2[i + n] = 0
            check3[n - i + N - 1] = 0


if __name__ == '__main__':
    N = int(input())
    check1 = [0] * N * 2
    check2 = [0] * N * 2
    check3 = [0] * N * 2
    cnt = 0
    bt(0)
    print(cnt)
