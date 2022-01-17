from collections import deque


def bfs():
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if state[nx][ny] == -1:
                    q.append((nx, ny))
                    state[nx][ny] = 0


if __name__ == '__main__':
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    check_list = []
    # max_num = 0
    # for i in range(N):
    #     for j in range(N):
    #         if max_num < graph[i][j]:
    #             max_num = graph[i][j]
    for flag in range(101):
        state = [[0] * N for _ in range(N)]
        check = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] > flag:
                    state[i][j] = -1
        for i in range(N):
            for j in range(N):
                if state[i][j] == -1:
                    state[i][j] = 0
                    q.append((i, j))
                    bfs()
                    check += 1
        check_list.append(check)
    print(max(check_list))
