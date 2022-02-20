def recur(x, y, n):
    global check
    num_check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != num_check:
                for k in range(2):
                    for m in range(2):
                        next_n = n // 2
                        recur(x + k * next_n, y + m * next_n, next_n)
                return

    if num_check == 0:
        check[0] += 1
    else:
        check[1] += 1


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    check = [0, 0]
    recur(0, 0, N)
    print(*check, sep='\n')
