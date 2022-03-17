import sys

mini = sys.maxsize


def bt(x, y, result, res):
    global mini
    if len(res) == N and graph[y][x]:
        mini = min(mini, result+graph[y][x])
        return
    for i in range(N):
        if graph[y][i] and i not in res:
            if result < mini:
                res.append(i)
                bt(x, i, result + graph[y][i], res)
                res.pop()


if __name__ == '__main__':
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    check = []
    for i in range(N):
        bt(i, i, 0, [i])
    print(mini)
