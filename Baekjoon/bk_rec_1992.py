def rec(x, y, n):
    check = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != graph[i][j]:
                print("(", end='')
                n = n // 2
                rec(x, y, n)
                rec(x, y + n, n)
                rec(x + n, y, n)
                rec(x + n, y + n, n)
                print(")", end='')
                return
    if check == 1:
        print(1, end='')
        return
    else:
        print(0, end='')
        return


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input())) for _ in range(N)]
    rec(0, 0, N)
