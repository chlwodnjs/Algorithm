def bt(x):
    if len(graph) == M:
        print(*graph)
        return
    else:
        for i in range(x, N + 1):
            graph.append(i)
            bt(i)
            graph.pop()


if __name__ == '__main__':
    N, M = map(int, input().split())
    graph = []
    bt(1)

# def bt(x):
#     if x == M:
#         if sorted(graph) == graph:
#             print(*graph)
#     else:
#         for i in range(1, N + 1):
#             graph.append(i)
#             bt(x + 1)
#             graph.pop()
#
#
# if __name__ == '__main__':
#     N, M = map(int, input().split())
#     graph = []
#     bt(0)
