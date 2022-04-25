def sim():
    for i in range(N ** 2):
        numarr = list(map(int, input().split()))
        dic[numarr[0]] = numarr[1:]
        mx, my, check1, check2 = 0, 0, -1, -1
        for j in range(N):
            for k in range(N):
                if not graph[j][k]:
                    cnt1, cnt2 = 0, 0
                    for m in range(4):
                        nx = j + dx[m]
                        ny = k + dy[m]
                        if 0 <= nx < N and 0 <= ny < N:
                            if graph[nx][ny] in dic[numarr[0]]:
                                cnt1 += 1
                            if not graph[nx][ny]:
                                cnt2 += 1
                    if check1 < cnt1 or (check1 == cnt1 and check2 < cnt2):
                        mx = j
                        my = k
                        check1 = cnt1
                        check2 = cnt2
        graph[mx][my] = numarr[0]




if __name__ == "__main__":
    N = int(input())
    graph = [[0] * N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dic = {}
    res = 0
    sim()

    for x in range(N):
        for y in range(N):
            flag = 0
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] in dic[graph[x][y]]:
                        flag += 1
            if flag:
                res += 10 ** (flag - 1)
    print(res)
