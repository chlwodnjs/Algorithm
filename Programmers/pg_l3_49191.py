def solution(n, results):
    answer = 0
    graph = [[None] * n for _ in range(n)]
    for i in results:
        graph[i[0] - 1][i[1] - 1] = 1
        graph[i[1] - 1][i[0] - 1] = 0

    for i in range(n):
        for j in range(n):
            for k in range(n):
                if graph[j][i] is not None and graph[j][i] == graph[i][k]:
                    graph[j][k] = graph[j][i]
                    graph[k][j] = not graph[j][i]

    for i in range(n):
        if None not in graph[i][:i] + graph[i][i + 1:]:
            answer += 1

    return answer