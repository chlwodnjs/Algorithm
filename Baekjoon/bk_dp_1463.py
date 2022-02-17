from collections import deque


def dp():
    for i in range(2, N + 1):
        graph[i] = graph[i - 1] + 1
        if i % 2 == 0:
            graph[i] = min(graph[i], graph[i // 2] + 1)
        if i % 3 == 0:
            graph[i] = min(graph[i], graph[i // 3] + 1)
    return graph[N]


if __name__ == '__main__':
    N = int(input())
    graph = [0] * (N + 1)
    print(dp())
