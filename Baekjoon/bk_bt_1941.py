from collections import deque


def bt(arr, S, Y):
    if Y > 3:
        return
    if len(arr) == 7:
        arr.sort()
        res.add(tuple(arr))
    else:
        q = deque()
        for node in range(len(arr)):
            for k in range(4):
                nx = arr[node][0] + dx[k]
                ny = arr[node][1] + dy[k]
                if 0 > nx or 5 <= nx or 0 > ny or 5 <= ny: continue
                if (nx, ny) in arr: continue
                q.append((nx, ny))
        for i in range(len(q)):
            x = q[i][0]
            y = q[i][1]
            if graph[x][y] == 'S':
                bt(arr + [(x, y)], S + 1, Y)
            else:
                bt(arr + [(x, y)], S, Y + 1)


if __name__ == '__main__':
    graph = [list(map(str, input())) for _ in range(5)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    res = set()
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'S':
                bt([(i, j)], 1, 0)
    print(len(res))
