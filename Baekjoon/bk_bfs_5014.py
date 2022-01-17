from collections import deque


def bfs():
    while q:
        s = q.popleft()
        for k in range(2):
            ns = s + dx[k]
            if 0 <= ns < F and check_list[ns] == -1:
                q.append(ns)
                check_list[ns] = check_list[s]+1
    if check_list[G - 1] != -1:
        return check_list[G-1]
    else:
        return 'use the stairs'


if __name__ == '__main__':
    F, S, G, U, D = map(int, input().split())
    q = deque()
    dx = [U, -D]
    check_list = [-1 for _ in range(F)]
    q.append(S - 1)
    check_list[S - 1] = 0
    print(bfs())
