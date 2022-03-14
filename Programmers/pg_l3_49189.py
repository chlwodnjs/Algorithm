from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    q = deque([1])
    visited[1] = 1

    while q:
        x = q.popleft()
        for k in graph[x]:
            if not visited[k]:
                visited[k] = visited[x] + 1
                q.append(k)

    check = max(visited)
    for i in visited:
        if i == check:
            answer += 1
    return answer