from collections import deque


def bfs():
    while q2:
        x1, y1 = q2.popleft()

        for k1 in range(4):
            mx = x1 + dx[k1]
            my = y1 + dy[k1]

            if 0 <= mx < H and 0 <= my < W:
                if graph[mx][my]!='#' and fire[mx][my]==-1:  # 불이 붙을 수 있는 곳
                    fire[mx][my] = fire[x1][y1] + 1
                    q2.append((mx, my))
    while q1:
        x, y = q1.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < H and 0 <= ny < W:
                if sg[nx][ny]==-1 and graph[nx][ny] == '.': # 이동가능한
                    if fire[nx][ny]==-1 or fire[nx][ny] > sg[x][y] + 1: # 불이 아니고 불보다 빨리
                        sg[nx][ny] = sg[x][y] + 1
                        q1.append((nx, ny))
            else:
                return sg[x][y] + 2

    return "IMPOSSIBLE"


if __name__ == '__main__':
    dx=[1,0,-1,0]
    dy=[0,1,0,-1]

    T = int(input())

    for i in range(T):
        W,H = map(int,input().split())
        q1=deque()
        q2=deque()
        graph = [list(map(str,input())) for _ in range(H)]
        sg = [[-1] * W for _ in range(H)]
        fire = [[-1] * W for _ in range(H)]
        for h in range(H):
            for w in range(W):
                if graph[h][w]=='@':
                    q1.append((h,w))
                elif graph[h][w]=='*':
                    q2.append((h,w))

        print(bfs())
