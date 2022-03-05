import sys
from itertools import combinations


def bt():
    for comb in check:
        visited = [0] * N
        s_list = []
        l_list = []
        for i in comb:
            visited[i] = 1
            s_list.append(i)

        for i in range(N):
            if not visited[i]:
                l_list.append(i)

        s_value = 0
        l_value = 0
        for i in range(L):
            for j in range(L):
                if graph[s_list[i]][s_list[j]]:
                    s_value += graph[s_list[i]][s_list[j]]
                if graph[l_list[i]][l_list[j]]:
                    l_value += graph[l_list[i]][l_list[j]]
        res.append(abs(s_value - l_value))

    return min(res)


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    N_list = [i for i in range(N)]
    L = N // 2
    check = list(combinations(N_list, L))
    res = []
    print(bt())
#
# def bt(count, index):
#     global check_value
#     if index == N:
#         return
#     if count == N // 2:
#         temp = 0
#         for i in range(N):
#             for j in range(N):
#                 if check[i] and check[j]:
#                     temp += graph[i][j]
#                 if not check[i] and not check[j]:
#                     temp -= graph[i][j]
#         check_value = min(abs(temp), check_value)
#         return
#     check[index] = 1
#     bt(count + 1, index + 1)
#     check[index] = 0
#     bt(count, index + 1)
#
#
# if __name__ == '__main__':
#     N = int(input())
#     graph = list(list(map(int, input().split())) for _ in range(N))
#
#     check = [0] * N
#     check_value = sys.maxsize
#
#     bt(0, 0)
#     print(check_value)
