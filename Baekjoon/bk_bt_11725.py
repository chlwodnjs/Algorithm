import sys

sys.setrecursionlimit(10 ** 6)


def bt(x):
    for i in graph[x]:
        if res[i] == 0:
            res[i] = x
            bt(i)


if __name__ == '__main__':
    N = int(input())
    graph = [[0] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = [0] * (N + 1)
    bt(1)
    res.pop(0)
    res.pop(0)
    print(*res, sep='\n')
