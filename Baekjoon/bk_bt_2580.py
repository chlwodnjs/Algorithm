def is_check(i, j):
    check = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if graph[i][k] in check:
            check.remove(graph[i][k])
        if graph[k][j] in check:
            check.remove(graph[k][j])

    i //= 3
    j //= 3
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if graph[p][q] in check:
                check.remove(graph[p][q])

    return check


def bt(x):
    if x == len(check_0):
        for row in graph:
            print(*row)
        exit(0)

    (i, j) = check_0[x]
    check = is_check(i, j)

    for num in check:
        graph[i][j] = num
        bt(x + 1)
        graph[i][j] = 0


if __name__ == '__main__':
    graph = [list(map(int, input().split())) for _ in range(9)]
    check_0 = []
    for i in range(9):
        for j in range(9):
            if graph[i][j] == 0:
                check_0.append((i, j))
    bt(0)
