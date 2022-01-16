from collections import deque


def bfs():
    check = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if n_graph[nx][ny] == 1:
                    check += 1
                    n_graph[nx][ny] = 0
                    q.append((nx, ny))
    return check_list.append(check)


if __name__ == '__main__':
    N = int(input())
    q = deque()
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    check_list = []
    n_graph = [list(map(int, input())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # if n_graph[j][i] == 1:
            #     q.append((j, i))
            #     n_graph[j][i]=0
            #     bfs()
            if n_graph[i][j] == 1:
                q.append((i, j))
                n_graph[i][j] = 0
                bfs()
    len_check = len(check_list)
    print(len_check)

    for i in range(len_check):
        print(sorted(check_list)[i])
