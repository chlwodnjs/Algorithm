from itertools import combinations
import sys


def sim():
    res = sys.maxsize
    for comb in combinations(check2, M):
        check = 0
        for x in check1:
            check += min([abs(x[0] - i[0]) + abs(x[1] - i[1]) for i in comb])
            if res <= check:
                break
        if check < res:
            res = check
    return res


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]

    check1 = []
    check2 = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                check1.append((i, j))
            elif graph[i][j] == 2:
                check2.append((i, j))
    print(sim())
