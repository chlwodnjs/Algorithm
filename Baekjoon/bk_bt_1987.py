import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def bt(x, y, flag):
    global res
    res = max(res, flag)
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < R and 0 <= ny < C:
            if not check[graph[nx][ny]]:
                check[graph[nx][ny]] = 1
                bt(nx, ny, flag + 1)
                check[graph[nx][ny]] = 0


if __name__ == '__main__':
    R, C = map(int, input().split())
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res = 1
    graph = [list(map(lambda i: ord(i) - 65, input())) for _ in range(R)]
    check = [0] * 26
    check[graph[0][0]] = 1
    bt(0, 0, 1)
    print(res)

#
# def bfs():
#     result = 1
#     check = set([(0, 0, graph[0][0])])
#
#     while check:
#         x, y, visited = check.pop()
#
#         for k in range(4):
#             nx = x + dx[k]
#             ny = y + dy[k]
#             if 0 <= nx < R and 0 <= ny < C:
#
#                 if graph[nx][ny] not in visited:
#                     next_visited = visited + graph[nx][ny]
#                     check.add((nx, ny, next_visited))
#                     result = max(result, len(next_visited))
#
#     return result
#
#
# print(bfs())
