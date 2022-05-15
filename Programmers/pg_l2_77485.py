def solution(rows, columns, queries):
    answer = []
    graph = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            graph[i][j] = i * columns + j + 1

    for arr in queries:

        x1 = arr[0] - 1
        y1 = arr[1] - 1
        x2 = arr[2] - 1
        y2 = arr[3] - 1

        check = [graph[x1][y1]]

        for i in range(y1 + 1, y2 + 1):
            check.append(graph[x1][i])
            graph[x1][i] = check[-2]
        for i in range(x1 + 1, x2 + 1):
            check.append(graph[i][y2])
            graph[i][y2] = check[-2]
        for i in reversed(range(y1, y2)):
            check.append(graph[x2][i])
            graph[x2][i] = check[-2]
        for i in reversed(range(x1, x2)):
            check.append(graph[i][y1])
            graph[i][y1] = check[-2]

        answer.append(min(check))

    return answer