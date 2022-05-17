from collections import Counter
from functools import reduce


def sim():
    check = 0
    for i in range(len(graph)):
        dic = Counter(graph[i])
        del dic[0]
        dic = list(dic.items())
        dic.sort(key=lambda x: (x[1], x[0]))
        if len(dic) > 50:
            dic = dic[:50]
        graph[i] = reduce(lambda x, y: x + list(y), dic[1:], list(dic[0]))
        check = max(check, len(graph[i]))

    for i in range(len(graph)):
        if len(graph[i]) < check:
            graph[i].extend([0] * (check - len(graph[i])))


if __name__ == '__main__':
    a, b, k = map(int, input().split())
    res = 0
    graph = [list(map(int, input().split())) for _ in range(3)]

    while 1:

        if a - 1 < len(graph) and b - 1 < len(graph[0]):
            if graph[a - 1][b - 1] == k:
                print(res)
                break
        if res > 100:
            print(-1)
            break
        if len(graph) >= len(graph[0]):
            sim()
        elif len(graph) < len(graph[0]):
            graph = list(map(list, zip(*graph)))
            sim()
            graph = list(map(list, zip(*graph)))
        res += 1
